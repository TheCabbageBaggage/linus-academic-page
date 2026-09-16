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
echo "✓ deployed"
