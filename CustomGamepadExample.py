#!/usr/bin/env python
# coding: utf-8

# Load the gamepad and time libraries
import Gamepad
import time

# Make our own custom gamepad
# The numbers can be figured out by running the Gamepad script:
# ./Gamepad.py
# Press ENTER without typing a name to get raw numbers for each
# button press or axis movement, press CTRL+C when done
class CustomGamepad(Gamepad.Gamepad):
    def __init__(self, joystickNumber = 0):
        Gamepad.Gamepad.__init__(self, joystickNumber)
        self.axisNames = {
            0: 'LEFT-X',
            1: 'LEFT-Y',
            2: 'RIGHT-Y',
            3: 'RIGHT-X',
            4: 'DPAD-X',
            5: 'DPAD-Y'
        }
        self.buttonNames = {
            0:  '1',
            1:  '2',
            2:  '3',
            3:  '4',
            4:  'L1',
            5:  'L2',
            6:  'R1',
            7:  'R2',
            8:  'SELECT',
            9:  'START',
            10: 'L3',
            11: 'R3'
        }
        self._setupReverseMaps()

# Gamepad settings
gamepadType = CustomGamepad
buttonHappy = '3'
buttonBeep = 'L3'
buttonExit = 'START'
joystickSpeed = 'LEFT-Y'
joystickSteering = 'RIGHT-X'

# Wait for a connection
if not Gamepad.available():
    print('Please connect your gamepad...')
    while not Gamepad.available():
        time.sleep(1.0)
gamepad = gamepadType()
print('Gamepad connected')

# Set some initial state
speed = 0.0
steering = 0.0

# Handle joystick updates one at a time
while gamepad.isConnected():
    # Wait for the next event
    eventType, control, value = gamepad.getNextEvent()

    # Determine the type
    if eventType == 'BUTTON':
        # Button changed
        if control == buttonHappy:
            # Happy button (event on press and release)
            if value:
                print(':)')
            else:
                print(':(')
        elif control == buttonBeep:
            # Beep button (event on press)
            if value:
                print('BEEP')
        elif control == buttonExit:
            # Exit button (event on press)
            if value:
                print('EXIT')
                break
    elif eventType == 'AXIS':
        # Joystick changed
        if control == joystickSpeed:
            # Speed control (inverted)
            speed = -value
        elif control == joystickSteering:
            # Steering control (not inverted)
            steering = value
        print('%+.1f %% speed, %+.1f %% steering' % (speed * 100, steering * 100))
