from simple_websocket_server import WebSocketServer, WebSocket

kicked = True
encoding = 'windows-1252'
class SimpleEcho(WebSocket):
    def handle(self):
        # echo message back to client
        print(type(self.data))
        print(self.data.decode(encoding))
        #self.send_message(self.data)

    def connected(self):
        print(self.address, 'connected')
        kicked = False

    def handle_close(self):
        print(self.address, 'closed')
        kicked = True

while kicked:
    server = WebSocketServer('', 8081, SimpleEcho)
    server.serve_forever()
