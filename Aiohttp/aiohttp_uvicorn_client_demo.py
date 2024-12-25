# _*_ coding : utf-8 _*_
# @Author    : songtf
# @Time      : 2024/12/25 上午11:01
# @File      : aiohttp_uvicorn_client_demo.py
# @Desc      :


import aiohttp
from fastapi import FastAPI
import asyncio


async def req():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:8080/api') as resp:
            return await resp.json()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(req())
    print(result)
