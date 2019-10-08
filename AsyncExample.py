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
pollInterval = 0.1

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

# Start the background updating
gamepad.startBackgroundUpdates()

# Joystick events handled in the background
try:
    while gamepad.isConnected():
        # Check for the exit button
        if gamepad.beenPressed(buttonExit):
            print('EXIT')
            break

        # Check for happy button changes
        if gamepad.beenPressed(buttonHappy):
            print(':)')
        if gamepad.beenReleased(buttonHappy):
            print(':(')

        # Check if the beep button is held
        if gamepad.isPressed(buttonBeep):
            print('BEEP')

        # Update the joystick positions
        # Speed control (inverted)
        speed = -gamepad.axis(joystickSpeed)
        # Steering control (not inverted)
        steering = gamepad.axis(joystickSteering)
        print('%+.1f %% speed, %+.1f %% steering' % (speed * 100, steering * 100))

        # Sleep for our polling interval
        time.sleep(pollInterval)
finally:
    # Ensure the background thread is always terminated when we are done
    gamepad.disconnect()
