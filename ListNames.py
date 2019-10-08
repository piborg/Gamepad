#!/usr/bin/env python
# coding: utf-8

# Load the gamepad and time libraries
import Gamepad
import time

# Wait for a connection
if not Gamepad.available():
    print('Please connect your gamepad...')
    while not Gamepad.available():
        time.sleep(1.0)
print('Gamepad connected')

# Pick the gamepad type
#gamepad = Gamepad.Gamepad()   #Generic unnamed controls
#gamepad = Gamepad.PS3()
gamepad = Gamepad.PS4()

# Show the selected gamepad type
print('Gamepad type: ' + gamepad.__class__.__name__)

# Display axis names
axisNames = gamepad.availableAxisNames()
if axisNames:
    print('Available axis names:')
    for axis in axisNames:
        print('   ' + str(axis))
else:
    print('No axis name mappings configured')
print('')

# Display button names
buttonNames = gamepad.availableButtonNames()
if buttonNames:
    print('Available button names:')
    for button in buttonNames:
        print('   ' + str(button))
else:
    print('No button name mappings configured')
