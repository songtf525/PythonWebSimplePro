# _*_ coding : utf-8 _*_
# @Author    : songtf
# @Time      : 2024/12/25 上午10:28
# @File      : aiohttp_test_app.py
# @Desc      :


from aiohttp import web


async def hello(request):
    return web.Response(text="Hello, world!")


if __name__ == '__main__':
    app = web.Application()
    app.add_routes([web.get('/', hello)])
    web.run_app(app)
