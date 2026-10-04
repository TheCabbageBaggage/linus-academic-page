#!/usr/bin/env python3
"""
DOI / Reference-Verifikation (v2) — autoritativ.

Für jeden doi.org-Link:
  1. DOI Handle API  https://doi.org/api/handles/<doi>
     responseCode 1   = DOI registriert (existiert)
     responseCode 100 = Handle nicht gefunden (DOI falsch/tot)
  2. Crossref  https://api.crossref.org/works/<doi>
     liefert Titel/Journal/Jahr zur Plausibilitätsprüfung (nur bei registered)

Für non-DOI-URLs: HTTP HEAD/GET.

Klassifikation:
  OK          – DOI registriert / URL erreichbar (200/202)
  BLOCKED     – DOI registriert, aber Publisher blockt Bot (403)  -> kein Problem
  BROKEN      – DOI nicht registriert (Handle 100 / 404)          -> FIX NÖTIG
  RATE-LIMITED– 429/406
"""
import json
import re
import sys
import time
import urllib.request
import urllib.error
import ssl

SRC = "/data/.openclaw/workspace/projects/linus-academic-page/analysis/2026-10-01-executive-essays.md"
OUT_MD = "/data/.openclaw/workspace/projects/linus-academic-page/analysis/2026-10-01-doi-verification.md"
OUT_JSON = "/data/.openclaw/workspace/projects/linus-academic-page/analysis/2026-10-01-doi-verification.json"

UA = "ClowieReferenceCheck/1.0 (mailto:claw.clowie@gmail.com)"
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

URL_RE = re.compile(r"https?://[^\s<>\"'\]\)]+(?:\([0-9A-Za-z]\))?[^\s<>\"'\]]*")
# simpler & robust: take up to whitespace, then trim trailing punctuation
URL_RE = re.compile(r"https?://\S+")
ESSAY_RE = re.compile(r"^## (Essay \d+ — .+)$", re.M)


def http_get(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
        return r.status, r.read(200000).decode("utf-8", "replace")


def http_status(url, timeout=20):
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers={"User-Agent": UA, "Accept": "*/*"})
            with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
                return r.status, r.geturl()
        except urllib.error.HTTPError as e:
            if method == "GET":
                return e.code, url
            continue
        except Exception:
            if method == "GET":
                return None, url
            continue
    return None, url


def check_doi(doi):
    """Authoritative: handle API. Returns (registered:bool, note)."""
    api = "https://doi.org/api/handles/" + urllib.parse.quote(doi, safe="/()")
    for attempt in range(3):
        try:
            st, body = http_get(api)
            data = json.loads(body)
            rc = data.get("responseCode")
            if rc == 1:
                return True, "handle registered"
            if rc == 100:
                return False, "handle NOT found"
            return None, f"handle responseCode={rc}"
        except urllib.error.HTTPError as e:
            if e.code in (429, 406):
                time.sleep(2 * (attempt + 1))
                continue
            if e.code == 404:
                return False, "handle 404"
            return None, f"handle HTTP {e.code}"
        except Exception as e:
            time.sleep(1.5 * (attempt + 1))
            last = type(e).__name__
    return None, f"handle error {last}"


def check_crossref(doi):
    api = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/()")
    try:
        st, body = http_get(api)
        m = json.loads(body).get("message", {})
        title = (m.get("title") or [""])[0]
        year = ""
        for k in ("published-print", "published-online", "issued", "created"):
            if m.get(k, {}).get("date-parts"):
                year = m[k]["date-parts"][0][0]
                break
        return title[:120], year
    except Exception:
        return None, None


def split_essays(text):
    parts = ESSAY_RE.split(text)
    out = []
    for i in range(1, len(parts), 2):
        out.append((parts[i].strip(), parts[i + 1]))
    return out


def references_block(body):
    m = re.search(r"### References\s*\n(.*?)(?=\n---|\Z)", body, re.S)
    return m.group(1).strip() if m else ""


def ref_entries(block):
    return [e.strip() for e in re.split(r"\n\s*\n", block) if e.strip()]


def main():
    import urllib.parse  # noqa
    text = open(SRC, encoding="utf-8").read()
    essays = split_essays(text)
    results = []

    for title, body in essays:
        entries = ref_entries(references_block(body))
        essay_res = {"essay": title, "references": []}
        for entry in entries:
            if entry.lstrip("*").startswith("**Redaktioneller"):
                continue  # editorial note, not a reference
            urls = [u.rstrip(".,;") for u in URL_RE.findall(entry)]
            doi = next((u.split("doi.org/", 1)[1] for u in urls if "doi.org/" in u), None)
            non_doi = next((u for u in urls if "doi.org/" not in u), None)
            ym = re.search(r"\((\d{4}[a-z]?)\)", entry)
            rec = {
                "ref": entry.split("(")[0].strip()[:45],
                "year": ym.group(1) if ym else "",
                "doi": doi,
                "url": non_doi,
                "status": None, "http": None, "note": None, "title": None,
            }
            if doi:
                registered, note = check_doi(doi)
                rec["note"] = note
                if registered is True:
                    t, y = check_crossref(doi)
                    rec["title"] = t
                    if t and y and str(y) != rec["year"]:
                        rec["note"] += f"; Crossref-Jahr {y}"
                    rec["status"] = "OK"
                    rec["http"] = "handle:1"
                elif registered is False:
                    rec["status"] = "BROKEN"
                    rec["http"] = "handle:100"
                else:
                    rec["status"] = "UNVERIFIED"
                    rec["http"] = "—"
                time.sleep(0.3)
            elif non_doi:
                st, resolved = http_status(non_doi)
                rec["http"] = st
                if st in (200, 202):
                    rec["status"] = "OK"
                elif st in (403, 401):
                    rec["status"] = "BLOCKED"
                elif st in (429, 406):
                    rec["status"] = "RATE-LIMITED"
                else:
                    rec["status"] = "BROKEN"
                time.sleep(0.4)
            else:
                rec["status"] = "NO-URL"
            essay_res["references"].append(rec)
            print(f"  [{rec['status']:11}] {rec['ref'][:38]:38} {rec['year']:5} {doi or non_doi}", flush=True)
        results.append(essay_res)

    total = sum(len(e["references"]) for e in results)
    def cnt(s): return sum(1 for e in results for r in e["references"] if r["status"] == s)
    bad = [r for e in results for r in e["references"] if r["status"] in ("BROKEN", "UNVERIFIED", "NO-URL")]

    report = {"source": SRC, "total": total,
              "ok": cnt("OK"), "blocked": cnt("BLOCKED"), "rate_limited": cnt("RATE-LIMITED"),
              "broken": cnt("BROKEN"), "unverified": cnt("UNVERIFIED"), "no_url": cnt("NO-URL"),
              "essays": results}
    json.dump(report, open(OUT_JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    L = ["# DOI- und Referenz-Verifikation — Executive Essays", "",
         f"Quelle: `{SRC}`", "",
         f"**{total} Referenzen geprüft** — DOI-Prüfung autoritativ über die DOI-Handle-API "
         f"(registriert/nicht registriert), nicht über Publisher-HTTP (Publisher blocken Bots mit 403).", "",
         f"- ✅ **DOI registriert / URL erreichbar:** {cnt('OK')}",
         f"- 🟡 **Publisher blockt Bot (DOI registriert):** {cnt('BLOCKED')}",
         f"- ⚪ **Rate-limited:** {cnt('RATE-LIMITED')}",
         f"- ❌ **Nicht registriert / defekt:** {cnt('BROKEN')}",
         f"- ⚠️ **Nicht prüfbar:** {cnt('UNVERIFIED')}",
         f"- ➖ **Kein Link:** {cnt('NO-URL')}", ""]
    for e in results:
        L += [f"## {e['essay']}", "",
              "| Autor | Jahr | Status | Beweis | DOI/URL |", "|---|---|---|---|---|"]
        for r in e["references"]:
            link = ("https://doi.org/" + r["doi"]) if r["doi"] else (r["url"] or "—")
            L.append(f"| {r['ref']} | {r['year']} | {r['status']} | {r['http'] or '—'} | {link} |")
        L.append("")
    if bad:
        L += ["## Zu prüfen (defekt / nicht prüfbar)", ""]
        for r in bad:
            L.append(f"- **{r['status']}** — {r['ref']} {r['year']} — {r['doi'] or r['url']} — {r['note']}")
        L.append("")
    open(OUT_MD, "w", encoding="utf-8").write("\n".join(L))

    print(f"\nTOTAL={total} OK={cnt('OK')} BLOCKED={cnt('BLOCKED')} BROKEN={cnt('BROKEN')} "
          f"UNVERIFIED={cnt('UNVERIFIED')} NO_URL={cnt('NO-URL')}")
    return 0


if __name__ == "__main__":
    import urllib.parse  # noqa
    sys.exit(main())
