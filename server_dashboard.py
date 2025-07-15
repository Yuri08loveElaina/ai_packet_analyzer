from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()
html = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Packet Analyzer Dashboard</title>
</head>
<body>
    <h2>AI Packet Analyzer Dashboard</h2>
    <ul id="logs"></ul>
<script>
    let ws = new WebSocket("ws://localhost:8000/ws");
    ws.onmessage = function(event) {
        let logs = document.getElementById('logs');
        let li = document.createElement('li');
        li.innerText = event.data;
        logs.prepend(li);
    }
</script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def get_dashboard(request: Request):
    return html

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    from packet_sniffer import WS_CLIENTS
    WS_CLIENTS.add(websocket)
    try:
        while True:
            await websocket.receive_text()
    except:
        WS_CLIENTS.remove(websocket)

if __name__ == "__main__":
    uvicorn.run("server_dashboard:app", host="0.0.0.0", port=8000, reload=False)
