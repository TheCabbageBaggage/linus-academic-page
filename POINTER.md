# Linus Kohl — Academic Profile Page → moved to its own repository

**Repo:** https://github.com/TheCabbageBaggage/linus-academic-page

```bash
git clone git@github.com:TheCabbageBaggage/linus-academic-page.git
```

- **Live:** https://linus.cabbagebaggage.net
- **Deployed:** PROD (Hostinger, Traefik, `linus-page` container)
- **Stack:** static HTML/CSS, no build step
- **Deploy:** `./deploy.sh` — packages `site/`, uploads, restarts the container, verifies HTTP 200
- **Design:** ACTA palette, Petroleum `#2C5F7C` primary

## Contents
```
site/index.html          profile page
site/style.css           ACTA/Petroleum stylesheet
paper-outlines/          four detailed research paper outlines
deploy.sh                one-command deploy + verify
```

The paper outlines are also published on ClawHub under the `medium` category.

Extracted from this monorepo on 2026-09-16 (monorepo commits `4916677`, `9d261c1`).
No code is tracked here — this directory is git-ignored and contains only this pointer.
