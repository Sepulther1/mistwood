#!/usr/bin/env bash
set -euo pipefail
UNIT_DIR="$HOME/.config/systemd/user"
mkdir -p "$UNIT_DIR"

cat > "$UNIT_DIR/grove-editor-sync.service" <<'UNIT'
[Unit]
Description=Sync editor keybindings from repo

[Service]
Type=oneshot
ExecStart=%h/dev/mistwood-dev/tools/editor-sync.py
UNIT

cat > "$UNIT_DIR/grove-editor-sync.timer" <<'UNIT'
[Unit]
Description=Run editor keybinding sync on boot and hourly

[Timer]
OnBootSec=30s
OnUnitActiveSec=1h
Persistent=true

[Install]
WantedBy=timers.target
UNIT

systemctl --user daemon-reload
systemctl --user enable --now grove-editor-sync.timer
systemctl --user start grove-editor-sync.service
systemctl --user status grove-editor-sync.timer --no-pager
