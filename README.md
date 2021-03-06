# Python examples ⇴  Wekinator
> by Karen Palacio.

# Introduction
Wekinator is free software that is used for real time, interactive machine learning.
In this repo you'll find examples to use with [Wekinator](http://www.wekinator.org/)

...**made in Python**!

You can also find examples to integrate wekinator **with P5**!

# Installation
Create and install dependencies in a fresh virtualenv

`pip install -r requirements.txt`

# Usage
to use any example

`python3 <example_file_name>.py`
# Examples listing:

## ➼ Inputs:
- `sender.py`: simple 1 input sender. Sends a number to wekinator.
- `p5_examples/sketch.js`: 1 input sender. Sends mouseX as a string (WIP) (TODO: pls make it  a float)
- `p5_examples/re_router.py`: Receives p5 inputs from the broswer (through OSC/websockets) and sends them back to wekinator (through OSC/udp), mantaining channel information. Based on `p5_examples/server_websocket_osc.py`
- `p5_examples/router.py`: Receives 3 p5 inputs from the broswer (through OSC/websockets) and sends them back to blender (through OSC/udp), mantaining channel information. Based on `p5_examples/re_router.py`. Now with multichannel feature, this server allows to handle **many blender variables with p5**!

## ↜ Outputs:
- `server.py` : simple 1 output osc server to use as template. Just prints the recieved float, which can be a number from 0 to 1.
- `window.py`: waits for 3 outputs from wekinator. Takes 3 floats from [0,1] and transforms each to [0,256] int values, and draws the resulting color on a window!
- `p5_examples/server_websocket_osc.py`: 1 output osc server through websockets to listen to a p5 client. A template for future p5 integrations, and not a real weki output. (WIP)

