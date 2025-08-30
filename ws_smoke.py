# /home/atlantis/dev/mistwood-dev-dev/ws_smoke.py
import websocket

URL = "ws://localhost:4102"

print(f"Connecting to {URL} ...")
ws = websocket.create_connection(URL, timeout=5)
print("Connected OK.")

# Send something harmless. If the server doesn't echo, it's fine—we just want 'no crash'.
try:
    ws.send("help")
    try:
        msg = ws.recv()
        print("Received:", (msg[:200] + "...") if len(msg) > 200 else msg)
    except Exception as e:
        print("No immediate reply (that can be normal).", e)
finally:
    ws.close()
    print("Closed.")