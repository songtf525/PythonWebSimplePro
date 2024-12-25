# _*_ coding : utf-8 _*_
# @Author    : songtf
# @Time      : 2024/12/25 下午1:13
# @File      : aiohttp_post_req.py
# @Desc      :


import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        data = {'key': 'value'}
        headers = {'User-Agent': 'Mozilla/5.0'}
        async with session.post('https://www.baidu.com', headers=headers, timeout=10, data=data) as resp:
            print(await resp.text())


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
