# Mistwood Tauri Wrapper (Dev)

## Create app
npm create tauri-app@latest mistwood-tauri -- --manager npm --template vanilla
cd mistwood-tauri
npm install

## Minimal WS usage (src/main.js)
export const WS_URL = import.meta.env.VITE_MISTWOOD_WS_URL || "ws://localhost:8080/ws";
const ws = new WebSocket(WS_URL);
ws.onopen = () => console.log("WS open");
ws.onmessage = (e) => console.log("WS:", e.data);

## Env
echo 'VITE_MISTWOOD_WS_URL=ws://localhost:8080/ws' > .env

## Dev
npm run tauri dev