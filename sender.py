import argparse
import math
from termcolor import colored
from pythonosc import udp_client
import random
import time

def print_volume_handler(unused_addr, args, volume):
  print("[{0}] ~ {1}".format(args[0], volume))

def print_compute_handler(unused_addr, args, volume):
  try:
    print("[{0}] ~ {1}".format(args[0], args[1](volume)))
  except ValueError: pass

def my_thing():
    return random.choice([0,1])
    #print(colored(str(arg2),'green',attrs=["blink"]))

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=6448,
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  client = udp_client.SimpleUDPClient(args.ip, args.port)

  while True:
    thing = my_thing()
    client.send_message("/wek/inputs", float(thing))
    print(f'sent {thing}')
    time.sleep(1)




