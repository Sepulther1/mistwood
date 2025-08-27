# AI Onboarding — Mistwood (Contributor Edition)

## Access & Roles
- Request access: join our Discord/Slack, sign the Contributor Guidelines, and get added to the **mistwood-dev** repo with the **Contributor** role.
- You will **not** work on `mistwood` (stable) unless promoted to **Maintainer**.
- Protected areas require review (see below).

## Local Setup (first time)
```bash
# Linux/WSL + VS Code assumed
git clone https://github.com/<org>/mistwood-dev.git
cd mistwood-dev
python -m venv .venv && source .venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
python -m evennia -l start
xdg-open http://localhost:4105 2>/dev/null || true