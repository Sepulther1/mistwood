# Mistwood Capacitor Wrapper (Dev)

npm create @capacitor/app@latest
# App Name: Mistwood
# App ID: org.mistwood.app
cd mistwood
npm install

# Add WebSocket snippet (www/ws.js)
export const WS_URL = (window.MISTWOOD_WS_URL || "ws://10.0.2.2:8080/ws");
const ws = new WebSocket(WS_URL);
ws.onopen = () => console.log("WS open");
ws.onmessage = (e) => console.log("WS:", e.data);

# Android
npx cap add android
npx cap copy
npx cap open android