#!/usr/bin/env python
# coding: utf-8

# Load the libraries
import sys
import Gamepad
import time
sys.path.insert(0, "/home/pi/thunderborg")
import ThunderBorg

# Settings for the gamepad
gamepadType = Gamepad.PS4               # Class for the gamepad (e.g. Gamepad.PS3)
joystickSpeed = 'LEFT-Y'                # Joystick axis to read for up / down position
joystickSpeedInverted = True            # Set this to True if up and down appear to be swapped
joystickSteering = 'RIGHT-X'            # Joystick axis to read for left / right position
joystickSteeringInverted = False        # Set this to True if left and right appear to be swapped
buttonSlow = 'L2'                       # Joystick button for driving slowly whilst held
slowFactor = 0.5                        # Speed to slow to when the drive slowly button is held, e.g. 0.5 would be half speed
buttonFastTurn = 'R2'                   # Joystick button for turning fast
buttonExit = 'PS'                       # Joystick button to end the program
buttonFullBeamToggle = 'CROSS'          # Joystick button to toggle the LEDs between battery mode and fully white
interval = 0.05                         # Time between motor updates in seconds, smaller responds faster but uses more processor time

# Power settings
voltageIn = 1.2 * 10                    # Total battery voltage to the ThunderBorg
voltageOut = 12.0 * 0.95                # Maximum motor voltage, we limit it to 95% to allow the RPi to get uninterrupted power

# Setup the power limits
if voltageOut > voltageIn:
    maxPower = 1.0
else:
    maxPower = voltageOut / float(voltageIn)

# Setup the ThunderBorg
TB = ThunderBorg.ThunderBorg()
#TB.i2cAddress = 0x15                  # Uncomment and change the value if you have changed the board address
TB.Init()
if not TB.foundChip:
    boards = ThunderBorg.ScanForThunderBorg()
    if len(boards) == 0:
        print('No ThunderBorg found, check you are attached :)')
    else:
        print('No ThunderBorg at address %02X, but we did find boards:' % (TB.i2cAddress))
        for board in boards:
            print('    %02X (%d)' % (board, board))
        print('If you need to change the I²C address change the setup line so it is correct, e.g.')
        print('TB.i2cAddress = 0x%02X' % (boards[0]))
    sys.exit()
# Ensure the communications failsafe has been enabled!
failsafe = False
for i in range(5):
    TB.SetCommsFailsafe(True)
    failsafe = TB.GetCommsFailsafe()
    if failsafe:
        break
if not failsafe:
    print('Board %02X failed to report in failsafe mode!' % (TB.i2cAddress))
    sys.exit()

# Show battery monitoring settings
battMin, battMax = TB.GetBatteryMonitoringLimits()
battCurrent = TB.GetBatteryReading()
print('Battery monitoring settings:')
print('    Minimum  (red)     %02.2f V' % (battMin))
print('    Half-way (yellow)  %02.2f V' % ((battMin + battMax) / 2))
print('    Maximum  (green)   %02.2f V' % (battMax))
print('')
print('    Current voltage    %02.2f V' % (battCurrent))
print('')

# Setup the state shared with callbacks
global running
global fullBeam
running = True
fullBeam = False

# Create the callback functions
def exitButtonPressed():
    global running
    print('EXIT')
    running = False

def fullBeamButtonPressed():
    global fullBeam
    fullBeam = not fullBeam
    if fullBeam:
        TB.SetLedShowBattery(False)
        TB.SetLeds(1, 1, 1)
    else:
        TB.SetLedShowBattery(True)

# Wait for a connection
TB.MotorsOff()
TB.SetLedShowBattery(False)
TB.SetLeds(0, 0, 1)
waitingToggle = True
if not Gamepad.available():
    print('Please connect your gamepad...')
    while not Gamepad.available():
        time.sleep(interval * 4)
        waitingToggle = not waitingToggle
        if waitingToggle:
            TB.SetLeds(0, 0, 1)
        else:
            TB.SetLeds(0, 0, 0)
print('Gamepad connected')
gamepad = gamepadType()

# Start the background updating
gamepad.startBackgroundUpdates()
TB.SetLedShowBattery(True)

# Register the callback functions
gamepad.addButtonPressedHandler(buttonExit, exitButtonPressed)
gamepad.addButtonPressedHandler(buttonFullBeamToggle, fullBeamButtonPressed)

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

        # Work out the adjusted speed and steering
        if gamepad.isPressed(buttonSlow):
            finalSpeed = speed * slowFactor
        else:
            finalSpeed = speed
        if gamepad.isPressed(buttonFastTurn):
            finalSteering = steering * 2.0
        else:
            finalSteering = steering

        # Determine the drive power levels
        driveLeft = finalSpeed
        driveRight = finalSpeed
        if finalSteering < -0.05:
            # Turning left
            driveLeft *= 1.0 + finalSteering
        elif finalSteering > +0.05:
            # Turning right
            driveRight *= 1.0 - finalSteering

        # Set the motors to the new speeds
        TB.SetMotor1(driveRight * maxPower)
        TB.SetMotor2(driveLeft * maxPower)

        # Sleep for our motor change interval
        time.sleep(interval)
finally:
    # Ensure the background thread is always terminated when we are done
    gamepad.disconnect()

    # Turn the motors off
    TB.MotorsOff()

    # Set the LED to a dim red to indicate we have finished
    TB.SetCommsFailsafe(False)
    TB.SetLedShowBattery(False)
    TB.SetLeds(0.2, 0, 0)
