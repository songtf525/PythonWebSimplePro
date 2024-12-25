# _*_ coding : utf-8 _*_
# @Author    : songtf
# @Time      : 2024/12/25 上午10:35
# @File      : aiohttp_uvicorn_server_demo.py
# @Desc      :


import aiohttp
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/api")
async def api():
    print("helloworld111")
    async with aiohttp.ClientSession() as session:
        print("helloworld222")
        async with session.post("https://jsonplaceholder.typicode.com/posts") as resp:
            print("helloworld333")
            return await resp.json()


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)
