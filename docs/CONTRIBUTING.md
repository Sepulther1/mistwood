# Contributing to Mistwood

Inspired by long-running MUDs like **Icesus** (icesus.org), we aim for longevity, craftsmanship, and player joy. Whether you code, write lore, or test—welcome.

## Local Dev (Evennia)
```bash
# from your fork
git clone https://github.com/<you>/mistwood-dev
cd mistwood-dev
python -m venv .venv && source .venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements.txt

# dev ports
# telnet 4100 | web proxy 4101 | websocket 4102 | webserver 4105 | AMP 4106
python -m evennia -l start