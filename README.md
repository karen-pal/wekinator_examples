# Python - Wekinator
> by Karen Palacio.

# Introduction
Wekinator is free software that is used for real time, interactive machine learning.
In this repo you'll find examples to use with [Wekinator](http://www.wekinator.org/)
...made in Python!

# Installation 
Create and install dependencies in a fresh virtualenv
`pip install -r requirements.txt`

# Usage
to use any example 
`python3 <example_file_name>.py`
# Examples listing:

## Inputs:
- `sender.py`: simple 1 input sender. Sends a number to wekinator.
## Outputs:
- `server.py` : simple 1 output osc server to use as template. Just prints the recieved float, which can be a number from 0 to 1.
- `window.py`: waits for 3 outputs from wekinator. Takes 3 floats from [0,1] and transforms it to RGB compatible ints, to draw them on a window!
