# Tourguide: GitHub Actions keys & variables (patterns)

## Repository variables (non-secret)
Path: Repo → Settings → Secrets and variables → Actions → Variables tab
- Name: DEPLOY_HOST → Value: 127.0.0.1
- Name: DEPLOY_USER → Value: atlantis
- Name: DEPLOY_DIR  → Value: /home/atlantis/dev/mistwood-dev

## Repository secrets
Path: Repo → Settings → Secrets and variables → Actions → Secrets tab
- Name: DEPLOY_KEY → Value: (paste **private** key text)
