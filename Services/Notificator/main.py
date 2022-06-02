import json
import random
from collections import defaultdict

from aiohttp import web


class DummyWebSocket:
    async def send_str(self, s):
        pass


clients: dict = defaultdict(lambda: DummyWebSocket())


async def notification_handler(request):
    global clients
    post = await request.post()
    uuid = (await request.post()).get('uuid', None)

    await clients[uuid].send_str(post.get('message', None))

    return web.Response(status=200, text="ok")


async def client_handler(request):
    global clients
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    uuid = await ws.receive()
    uuid = uuid.data
    print(f"Client connected: {uuid}")
    clients[uuid] = ws

    async for msg in ws:
        pass

    print(f"Client disconnectd: {uuid}")

    clients[uuid] = DummyWebSocket()


app = web.Application()
app.add_routes([web.post('/notification', notification_handler),
                web.get('/client', client_handler),
                ])
web.run_app(app)
