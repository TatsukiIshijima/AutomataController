import asyncio
import ipget
import websockets


async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f" >{greeting}")

if __name__ == '__main__':

    try:
        ip = ipget.ipget().ipaddr("wlan0")
        start_server = websockets.serve(hello, f"{ip.split('/')[0]}", 8765)
        print(f"launch web socket server {ip.split('/')[0]}:8765")

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        asyncio.get_event_loop().close()