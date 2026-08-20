import asyncio
import websockets

url = "wss://meowmetry-app.dev1.mnt.group/ws"


# async def send(websocket):
#     async for message in websocket:
#         print("Received:", message)


# async def receive(websocket): 
#     while True:
#         message = await asyncio.to_thread(input, "Send: ")
#         await websocket.send(message)


# async def main():
#     async with websockets.connect(url) as websocket:
#         print("Connected")

#         await asyncio.gather(
#             receive(websocket),
#             send(websocket),
#         )
#         # async for message in websocket:
#         #     print("Received", message)


# asyncio.run(main())







import websocket
ws = websocket.create_connection(url)

print("Connected")

while True:
    message = ws.recv()
    print("Received:", message)

    user_input = input("Send: ")
    ws.send(user_input)