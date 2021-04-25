# from p5 to weki
# Note: adjust configs from weki to blender in weki
from simple_websocket_server import WebSocketServer, WebSocket
import struct

encoding = "windows-1252"

from pythonosc import udp_client

p5_port = 8081
weki_port = 6448
client = udp_client.SimpleUDPClient("127.0.0.1", weki_port)


class ReRouter(WebSocket):
    def handle(self):
        # osc channel
        channel = self.data[0:5].decode("utf-8")
        # message type
        msg_type = self.data[9:10].decode("utf-8")
        # get message
        number = struct.unpack(">f", self.data[12:])[0]
        print(
            "msg from " + channel + ". type: " + msg_type + ", with value:>>",
            round(number, 2),
        )
        # from p5 to weki
        print("Sending to weki ", channel)
        client.send_message(channel, round(float(number), 2))

    def connected(self):
        print(self.address, "connected")

    def handle_close(self):
        print(self.address, "closed")


while True:
    print(f"[*] I listen inputs from p5 in localhost:{p5_port}")
    print(f"[*] I reroute msgs to wekinator, in localhost:{weki_port}")
    server = WebSocketServer("", p5_port, ReRouter)
    server.serve_forever()
