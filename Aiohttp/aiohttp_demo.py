# _*_ coding : utf-8 _*_
# @Author    : songtf
# @Time      : 2024/12/25 上午11:19
# @File      : aiohttp_demo.py
# @Desc      :


from aiohttp import web
import asyncio


async def handle(request):
    name = request.match_info.get('name', 'Anonymous')
    text = "Hello, " + name
    return web.Response(text=text)


async def wshandler(request):
    ws = web.WebSocketResponse()
    print('ws', ws)
    await ws.prepare(request)

    async for msg in ws:
        print("msg: ", msg)
        if msg.type == web.WSMsgType.text:
            print("Got this txt")
            await ws.send_str("hello, {}".format(msg.data))
        elif msg.type == web.WSMsgType.binary:
            await  ws.send_bytes(msg.data)
        elif msg.type == web.WSMsgType.close:
            break

    return ws


if __name__ == '__main__':
    app = web.Application()
    app.add_routes([
        web.get('/', handle),
        web.get('/ws', wshandler),
        web.get('/{name}', handle)
    ])
    asyncio.run(web.run_app(app, host='0.0.0.0', port=8080))
