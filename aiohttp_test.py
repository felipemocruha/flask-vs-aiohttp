from aiohttp import web
import uvloop
import asyncio
from uuid import uuid4
import json


async def index(request):
    res = json.dumps(uuid4().hex)
    return web.Response(body=res)


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
app = web.Application()
app.router.add_get('/', index)
