# _*_ coding : utf-8 _*_
# @Author    : songtf
# @Time      : 2024/12/25 下午1:10
# @File      : aiohttp_get_req.py
# @Desc      :

"""
import aiohttp
import asyncio


async def main():
    try:
        async with aiohttp.ClientSession() as session:
            proxy = 'https://user:password@proxy-server:port'
            async with session.get('https://www.baidusss.com', proxy=proxy) as resp:
                print(await resp.text())
    except aiohttp.ClientError as err:
        print("An error occurred", err)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
"""

# asyncio + aiohttp 协程最佳用途是并发进行http请求，用于爬虫，但是requests库是IO阻塞的，所以用aiohttp配合最佳
import asyncio
import aiohttp


async def send_http(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print("HTTP Status: " + str(resp.status))
            print(await resp.text())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_http('https://api.github.com/events'))
    print("success")
