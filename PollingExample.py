#!/usr/bin/env python
# coding: utf-8

# Load the gamepad and time libraries
import Gamepad
import time

# Gamepad settings
gamepadType = Gamepad.PS4
buttonHappy = 'CROSS'
buttonBeep = 'CIRCLE'
buttonExit = 'PS'
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
