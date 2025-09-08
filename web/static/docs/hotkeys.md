# Grove Hotkeys

## Standard

- `ctrl+alt+e` → `workbench.action.tasks.runTask` (evennia:start)
- `ctrl+alt+x` → `workbench.action.tasks.runTask` (evennia:stop)
- `ctrl+alt+r` → `workbench.action.tasks.runTask` (evennia:restart)
- `ctrl+alt+t` → `workbench.action.tasks.runTask` (evennia:status)
- `ctrl+alt+l` → `workbench.action.tasks.runTask` (evennia:tail logs)
- `ctrl+alt+q` → `workbench.action.tasks.runTask` (evennia:stop logs tail)
- `ctrl+alt+f` → `workbench.action.tasks.runTask` (evennia:force-stop)
- `ctrl+alt+b` → `workbench.action.tasks.runTask` (evennia:open web)
- `ctrl+shift+r` → `-workbench.action.debug.restart`
- `ctrl+shift+d` → `-workbench.view.debug`
- `ctrl+shift+r` → `workbench.action.tasks.runTask` (dev: reload (Mistwood))
- `ctrl+shift+s` → `workbench.action.tasks.runTask` (dev: sync+reload)
- `ctrl+shift+g` → `workbench.action.tasks.runTask` (grove: sync grade)
- `ctrl+shift+t` → `workbench.action.tasks.runTask` (telemetry: timelapse)
- `ctrl+shift+d` → `workbench.action.tasks.runTask` (deploy: run workflow (self-hosted))
- `ctrl+shift+c` → `workbench.action.tasks.runTask` (caddy: validate+reload)

## Your extra hotkeys

- `ctrl+shift+r` → `workbench.action.tasks.runTask` (dev: reload (Evennia))
- `ctrl+shift=g` → `workbench.action.tasks.runTask` (grove: sync grade)

---

### Opt-out / local overrides
Create the file:

`/home/atlantis/dev/mistwood-dev/editor/vscode/keybindings.local.json`

Put `[]` to disable all repo defaults on this machine, or put your own bindings.
The sync tool merges **local overrides > repo defaults > your existing user keys**.
