# Linus Kohl — Academic Profile Page

**URL:** https://linus.cabbagebaggage.net — **LIVE & VERIFIED (2026-09-16)**
**Server:** PROD (Hostinger srv1535179, 187.124.178.155) · Traefik · Let's Encrypt TLS

## Stack
- Static HTML/CSS — no framework, no CMS, no build step
- Container: `linus-page` (nginx:alpine), Compose `/opt/linus-page/docker-compose.yml`
- Network: `ollama-xwy9_default` (Traefik), certresolver `letsencrypt`
- DNS: Cloudflare A-record `linus` → 187.124.178.155 (proxied, record id `cafb21f6a8121c50ac670e959d3f6bb6`)

## Design
- ACTA palette, **Petroleum `#2C5F7C` as primary** (navy `#1A3440`, teal `#3D8B8B` accents, off-white `#F5F6F7`)
- Light theme (matches the academic genre — Schumacher uses light)
- Responsive (860px / 560px breakpoints), print stylesheet, no horizontal overflow at 1280px

## Sections
Hero · Research (3 themes) · Research agenda (4 papers) · Publications · Industry · Teaching · Contact

## Publications (18 entries + preprint, verified against Google Scholar)
Built from Scholar profile `TV0wSeD6s2AC` (the share.google link resolves here).

- Journal & peer-reviewed articles: 7
- Conference papers: 5
- Book chapters & edited volumes: 4
- Dissertation & theses: 2
- Preprints: 1

Headline metrics on page: **18 publications · 260+ citations · h-index 7**

### Deliberately excluded
OpenAlex (author `A5007434492`) returned 2 records for a *different* Linus Kohl — a cultural-history project
("Schmankerl Time Machine", 2020 article + dataset) from LMU Munich. Not included.

### Citation counts
Scholar is the source of record. OpenAlex under-counts materially (e.g. CIRP Annals 2021: Scholar 54 vs OpenAlex 33).
Where Scholar exposes no count, the badge is omitted rather than guessed.

## Known gaps (verify when convenient)
- [ ] Publication **years** for some entries are approximate (IFIP APMS, IEEE ETFA, WGAB, Cranfield, dissertation) — Scholar shows no year on the collapsed profile view. DOI pages have the exact values.
- [ ] `voestalpine Krems GmbH` is named explicitly — confirm with corporate comms/media relations
- [ ] `linus.kohl@gmail.com` is the public address — confirm it's the intended one
- [ ] LinkedIn URL `linkedin.com/in/linus-kohl` was not verified
- [ ] Add 2026 publications as they appear
- [ ] Speaker/talk entries under "Talks & media" are currently generic placeholders

## Deploy

```bash
./deploy.sh
```

Packages `site/`, uploads to PROD (Hostinger), restarts the `linus-page` container, and verifies
HTTP 200 + publication count. Idempotent — safe to re-run.

Manual equivalent:

```bash
tar czf /tmp/linus-site.tgz -C site .
scp /tmp/linus-site.tgz root@187.124.178.155:/tmp/
ssh root@187.124.178.155 'tar xzf /tmp/linus-site.tgz -C /opt/linus-page/site && chown -R ubuntu:ubuntu /opt/linus-page/site && docker restart linus-page'
```

## Verify

```bash
curl -s -o /dev/null -w "%{http_code}\n" https://linus.cabbagebaggage.net/   # expect 200
curl -s https://linus.cabbagebaggage.net/ | grep -c pub-title                # expect 19
```

## Repo

`git@github.com:TheCabbageBaggage/linus-academic-page.git` — standalone, no build step.

```
site/index.html   single-page site
site/style.css    ACTA palette (Petroleum primary)
deploy.sh         one-command deploy + verify
```

This project was originally developed inside the `openclaw-workspace` monorepo
(commits `4916677`, `9d261c1`) and extracted here on 2026-09-16.
