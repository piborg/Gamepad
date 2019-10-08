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
global running
running = True
speed = 0.0
steering = 0.0

# Create some callback functions for single events
def happyButtonPressed():
    print(':)')

def happyButtonReleased():
    print(':(')

def exitButtonPressed():
    global running
    print('EXIT')
    running = False

# Start the background updating
gamepad.startBackgroundUpdates()

# Register the callback functions
gamepad.addButtonPressedHandler(buttonHappy, happyButtonPressed)
gamepad.addButtonReleasedHandler(buttonHappy, happyButtonReleased)
gamepad.addButtonPressedHandler(buttonExit, exitButtonPressed)

# Joystick events handled in the background
try:
    while running and gamepad.isConnected():
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
