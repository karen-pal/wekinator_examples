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
## ↜ Outputs:
- `server.py` : simple 1 output osc server to use as template. Just prints the recieved float, which can be a number from 0 to 1.
- `window.py`: waits for 3 outputs from wekinator. Takes 3 floats from [0,1] and transforms each to [0,256] int values, and draws the resulting color on a window!
- `p5_examples/server_websocket_osc.py`: 1 output osc server through websockets to listen to a p5 client. A template for future p5 integrations. (WIP)
