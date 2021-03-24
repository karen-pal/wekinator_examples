from simple_websocket_server import WebSocketServer, WebSocket
import struct
kicked = True
encoding = 'windows-1252'
class SimpleEcho(WebSocket):
    def handle(self):
        thing = struct.unpack('>f', self.data[12:])
        print(thing[0])
        #self.send_message(self.data)

    def connected(self):
        print(self.address, 'connected')
        kicked = False

    def handle_close(self):
        print(self.address, 'closed')
        kicked = True

while kicked:
    print("[*] Serving in localhost:8081")
    server = WebSocketServer('', 8081, SimpleEcho)
    server.serve_forever()
