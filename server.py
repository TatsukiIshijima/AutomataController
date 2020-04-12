import asyncio
import ipget
import websockets


async def __receive_command(websocket, path):
    command = await websocket.recv()
    if command is not None:
        print(f"> receive {command}")

if __name__ == '__main__':

    try:
        ip = ipget.ipget().ipaddr("wlan0")
        start_server = websockets.serve(__receive_command, f"{ip.split('/')[0]}", 8765)
        print(f"launch web socket server {ip.split('/')[0]}:8765")

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        asyncio.get_event_loop().close()