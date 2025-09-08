# Trailguide

Trailguide is your step-by-step path to get Mistwood running and to learn the loop:
**Grove** (project data), **Canopy** (automation), **Kaliana Loop** (our review rhythm for human cadence accompanied by AI of your choice).

## 1) Install the basics
- Ubuntu 22.04+ (or WSL2 in PowerShell with same)
- Python 3.12, Git, Node.js 22, ffmpeg
- `git clone https://github.com/Sepulther1/mistwood.git && cd mistwood`
- `python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`

## 2) Start Mistwood locally
- `pip install evennia
- `evennia --init
- `evennia start` (first run)
- `python -m evennia -l reload` (reload while iterating)
- Web UI: http://127.0.0.1:4105/

## 3) Grove: get a grade
- `python tools/grove_sync.py` fills `web/static/telemetry/grade.json`
- Open `/dashboard/` to see your grade and hints as they pertain to relevant areas of utilizing this system to play a game, learn to code, and build something of your own within our ecosystem.
- `Open http://127.0.0.1:4105/dashboard/

## 4) Canopy: generate timelapse
- `tools/timelapse.sh && tools/publish_timelapse.sh`
- Open `/timelapse/` to view the videos. These will represent your progress within our ecosystem, in contrast to the growth of the entire organization.

## 5) Kaliana Loop: the cadence
- At the **start and end** of a workflow block, run the VS Code task:
  **Terminal → Run Task → “canopy: refresh grade & timelapse”**.
- Review `/dashboard/`, make decisions, commit. This will be something like a simplified project management system, but geared toward having fun, so gamified as per quests.

## 6) CI optional: push & deploy
- Push to `main`, `chore/**`, or `feat/**` to run **timelapse-and-telemetry**.
- Add secrets/variables for deploy (see README notes) to ship MP4s to the server
  and auto-reload Mistwood.

## 7) Where to look next
- `web/website/views.py` and templates under `web/website/templates/website/`
- `tools/` for generators and sync scripts
- Open an issue with “Trailguide” in the title if anything is unclear. The idea is to work with AI to help you play and develop with others that are doing the same. Have fun, don't stress, and treat everyone as you would a family member or friend.