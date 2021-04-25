# p5 to blender
# multichannel
from simple_websocket_server import WebSocketServer, WebSocket
import struct

encoding = "windows-1252"

from pythonosc import udp_client

p5_port = 8081
blender_port = 9001
# blender_channel = '/objects/Sphere/modifiers/Wireframe/thickness'
client = udp_client.SimpleUDPClient("127.0.0.1", blender_port)

blender_channels = {
    "/thic": "/objects/Sphere/modifiers/Wireframe/thickness",
    "/offs": "/objects/Sphere/modifiers/Wireframe/offset",
    "/heig": "/objects/Sphere/modifiers/Wave/height",
}


class SimpleRouter(WebSocket):
    def handle(self):
        # osc channel
        channel = self.data[0:5].decode("utf-8")
        print(channel)
        if channel not in blender_channels.keys():
            print(f"[***] Bad channel name: {channel}")
            return
        # message type
        msg_type = self.data[9:10].decode("utf-8")
        # get message
        number = struct.unpack(">f", self.data[12:])[0]
        print(
            "msg from " + channel + ". type: " + msg_type + ", with value:>> ",
            round(number, 2),
        )
        # from p5 to weki
        print("[*] Sending to blender ", blender_channels[channel])
        client.send_message(blender_channels[channel], round(float(number), 2))

    def connected(self):
        print(self.address, "connected")

    def handle_close(self):
        print(self.address, "closed")


while True:
    print(f"[*] I listen inputs from p5 in localhost:{p5_port}")
    print(f"[*] I reroute msgs to wekinator, in localhost:{blender_port}")
    server = WebSocketServer("", p5_port, SimpleRouter)
    server.serve_forever()
