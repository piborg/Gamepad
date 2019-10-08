#!/usr/bin/env python
# coding: utf-8

# Load the libraries
import sys
import Gamepad
import time
sys.path.insert(0, "/home/pi/rockyborg")
import RockyBorg

# Settings for the gamepad
gamepadType = Gamepad.PS4               # Class for the gamepad (e.g. Gamepad.PS3)
joystickSpeed = 'LEFT-Y'                # Joystick axis to read for up / down position
joystickSpeedInverted = True            # Set this to True if up and down appear to be swapped
joystickSteering = 'RIGHT-X'            # Joystick axis to read for left / right position
joystickSteeringInverted = False        # Set this to True if left and right appear to be swapped
buttonSlow = 'L2'                       # Joystick button for driving slowly whilst held
slowFactor = 0.5                        # Speed to slow to when the drive slowly button is held, e.g. 0.5 would be half speed
buttonExit = 'PS'                       # Joystick button to end the program
interval = 0.05                         # Time between motor updates in seconds, smaller responds faster but uses more processor time

# Power settings
voltageIn = 1.2 * 8                     # Total battery voltage to the RockyBorg
voltageOut = 6.0                        # Maximum motor voltage

# Setup the power limits
if voltageOut > voltageIn:
    maxPower = 1.0
else:
    maxPower = voltageOut / float(voltageIn)

# Setup the RockyBorg
RB = RockyBorg.RockyBorg()
#RB.i2cAddress = 0x21                  # Uncomment and change the value if you have changed the board address
RB.Init()
if not RB.foundChip:
    boards = RockyBorg.ScanForRockyBorg()
    if len(boards) == 0:
        print('No RockyBorg found, check you are attached :)')
    else:
        print('No RockyBorg at address %02X, but we did find boards:' % (RB.i2cAddress))
        for board in boards:
            print('    %02X (%d)' % (board, board))
        print('If you need to change the I²C address change the setup line so it is correct, e.g.')
        print('RB.i2cAddress = 0x%02X' % (boards[0]))
    sys.exit()

# Enable the motors and disable the failsafe
RB.SetCommsFailsafe(False)
RB.MotorsOff()
RB.SetMotorsEnabled(True)

# Setup the state shared with callbacks
global running
running = True

# Create the callback functions
def exitButtonPressed():
    global running
    print('EXIT')
    running = False

# Wait for a connection
RB.MotorsOff()
RB.SetLed(True)
waitingToggle = True
if not Gamepad.available():
    print('Please connect your gamepad...')
    while not Gamepad.available():
        time.sleep(interval * 4)
        waitingToggle = not waitingToggle
        if waitingToggle:
            RB.SetLed(False)
        else:
            RB.SetLed(True)
print('Gamepad connected')
gamepad = gamepadType()

# Start the background updating
gamepad.startBackgroundUpdates()
RB.SetLed(True)

# Register the callback functions
gamepad.addButtonPressedHandler(buttonExit, exitButtonPressed)

# Keep running while joystick updates are handled by the callbacks
try:
    while running and gamepad.isConnected():
        # Read the latest speed and steering
        if joystickSpeedInverted:
            speed = -gamepad.axis(joystickSpeed)
        else:
            speed = +gamepad.axis(joystickSpeed)
        if joystickSteeringInverted:
            steering = -gamepad.axis(joystickSteering)
        else:
            steering = +gamepad.axis(joystickSteering)

        # Work out the adjusted speed
        if gamepad.isPressed(buttonSlow):
            finalSpeed = speed * slowFactor
        else:
            finalSpeed = speed

        # Determine the drive power levels based on steering angle
        servoPosition = steering
        driveLeft = finalSpeed
        driveRight = finalSpeed
        if steering < -0.05:
            # Turning left
            driveLeft *= 1.0 + (0.5 * steering)
        elif steering > +0.05:
            # Turning right
            driveRight *= 1.0 - (0.5 * steering)

        # Set the motors to the new speeds and tilt the servo to steer
        RB.SetMotor1(-driveLeft * maxPower)
        RB.SetMotor2(driveRight * maxPower)
        RB.SetServoPosition(servoPosition)

        # Sleep for our motor change interval
        time.sleep(interval)
finally:
    # Ensure the background thread is always terminated when we are done
    gamepad.disconnect()

    # Turn the motors off
    RB.MotorsOff()

    # Turn the LED off indicate we have finished
    RB.SetLed(False)
