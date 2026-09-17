#!/usr/bin/env bash
# Deploy the site to PROD (Hostinger) — linus.cabbagebaggage.net
set -euo pipefail

SERVER="root@187.124.178.155"
REMOTE_SITE="/opt/linus-page/site"
LOCAL_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "→ packaging site/ …"
tar czf /tmp/linus-site.tgz -C "$LOCAL_DIR/site" .

echo "→ uploading to $SERVER …"
scp -q /tmp/linus-site.tgz "$SERVER:/tmp/"

echo "→ extracting + restarting container …"
ssh "$SERVER" "tar xzf /tmp/linus-site.tgz -C $REMOTE_SITE && chown -R ubuntu:ubuntu $REMOTE_SITE && docker restart linus-page"

echo "→ verifying …"
code=$(curl -s -o /dev/null -w '%{http_code}' https://linus.cabbagebaggage.net/)
pubs=$(curl -s https://linus.cabbagebaggage.net/ | grep -c 'pub-title')
echo "   HTTP $code · $pubs publication entries"
[ "$code" = "200" ] || { echo "✗ deploy failed"; exit 1; }

# HTML/CSS are served via Cloudflare with cache-control max-age=14400.
# A stale style.css at the edge + fresh index.html = visibly broken page.
# Always purge after deploy so the edge can't serve old CSS.
if command -v python3 >/dev/null && [ -n "${CF_API_TOKEN:-}" ]; then
  echo "→ purging Cloudflare cache …"
  python3 - "$CF_API_TOKEN" <<'PY'
import json, sys, urllib.request
zone, token = "7ce3959352fd1d35e77713493c5efb68", sys.argv[1]
url = f"https://api.cloudflare.com/client/v4/zones/{zone}/purge_cache"
body = json.dumps({"files": [
  "https://linus.cabbagebaggage.net/",
  "https://linus.cabbagebaggage.net/index.html",
  "https://linus.cabbagebaggage.net/style.css",
]}).encode()
req = urllib.request.Request(url, data=body, method="POST",
  headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
print("   purge:", json.load(urllib.request.urlopen(req)).get("success"))
PY
else
  echo "⚠ CF_API_TOKEN not set — remember to purge https://linus.cabbagebaggage.net/style.css"
fi

echo "✓ deployed"
