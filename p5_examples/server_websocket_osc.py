from simple_websocket_server import WebSocketServer, WebSocket
import struct
kicked = True
encoding = 'windows-1252'
class SimpleEcho(WebSocket):
    def handle(self):
        # get osc channel
        channel = self.data[0:5].decode('utf-8')
        # get message type
        msg_type = self.data[9:10].decode('utf-8')
        #get number
        number = struct.unpack('>f', self.data[12:])[0]
        print("msg from "+channel+ ". type: "+msg_type +", with value:>>", number)
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
