# Editors Integration (VS Code / Neovim / Emacs)

## VS Code extension (build)
```bash
cd /home/atlantis/dev/mistwood-dev/client/vscode-grove
npm install
npm run compile || npx esbuild src/extension.ts --bundle --outfile=dist/extension.js --platform=node --sourcemap --external:vscode
```

## VS Code run (F5)
- Open the extension folder, choose **Run Grove Extension**, press F5.

## WFB quick task (Ctrl+Alt+W)
- .vscode/tasks.json calls tools/wfb/new_wfb2.sh

## Neovim
- file: tools/editors/nvim/grove.lua
  :luafile /home/atlantis/dev/mistwood-dev/tools/editors/nvim/grove.lua
  :lua require("grove").GroveChat()

## Emacs
- file: tools/editors/emacs/grove.el
  (load-file "/home/atlantis/dev/mistwood-dev/tools/editors/emacs/grove.el")
  M-x grove-chat
