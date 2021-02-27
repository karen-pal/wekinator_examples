import pygame, sys
import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server

pygame.init()
screen = pygame.display.set_mode([800,600])
white = [255, 255, 255]
screen.fill(white)
pygame.display.set_caption("3 outputs - R G B - localhost:12000")
pygame.display.flip()

def update_color(args,R,G,B):
    print(int(R*256),int(G*256),int(B*256))
    screen.fill([int(R*256),int(G*256),int(B*256)])
    pygame.display.update()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
      default="127.0.0.1", help="The ip to listen on")
    parser.add_argument("--port",
      type=int, default=12001, help="The port to listen on")
    args = parser.parse_args()
    dispatcher = dispatcher.Dispatcher()
    #dispatcher.map("/wek/outputs", update_color, R, G, B)
    dispatcher.map("/wek/outputs", update_color)

    server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
