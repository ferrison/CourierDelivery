import json
import random
from collections import defaultdict

from aiohttp import web

courier_to_clients = defaultdict(list)


async def websocket_handler(request):
    global courier_to_clients
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    uuid = await ws.receive()
    uuid = uuid.data
    print(f"Courier connected: {uuid}")

    async for msg in ws:
        print(msg)
        for c in courier_to_clients[uuid]:
            await c.send_str(msg.data)


async def client_handler(request):
    global courier_to_clients
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    uuid = await ws.receive()
    uuid = uuid.data
    print(f"Client connected: {uuid}")
    courier_to_clients[uuid].append(ws)

    async for msg in ws:
        pass

    print(f"Client disconnectd: {uuid}")

    courier_to_clients[uuid].remove(ws)


app = web.Application()
app.add_routes([web.get('/courier', websocket_handler),
                web.get('/client', client_handler),
                ])
web.run_app(app)
