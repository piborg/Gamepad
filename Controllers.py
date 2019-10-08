# coding: utf-8
"""
Standard gamepad mappings.

Pulled in to Gamepad.py directly.
"""


class PS3(Gamepad):
    fullName = 'PlayStation 3 controller'

    def __init__(self, joystickNumber = 0):
        Gamepad.__init__(self, joystickNumber)
        self.axisNames = {
            0: 'LEFT-X',
            1: 'LEFT-Y',
            2: 'L2',
            3: 'RIGHT-X',
            4: 'RIGHT-Y',
            5: 'R2'
        }
        self.buttonNames = {
            0:  'CROSS',
            1:  'CIRCLE',
            2:  'TRIANGLE',
            3:  'SQUARE',
            4:  'L1',
            5:  'R1',
            6:  'L2',
            7:  'R2',
            8:  'SELECT',
            9:  'START',
            10: 'PS',
            11: 'L3',
            12: 'R3',
            13: 'DPAD-UP',
            14: 'DPAD-DOWN',
            15: 'DPAD-LEFT',
            16: 'DPAD-RIGHT'
        }
        self._setupReverseMaps()


# PS3 controller settings for older Raspbian versions
#class PS3(Gamepad):
#    fullName = 'PlayStation 3 controller'
#
#    def __init__(self, joystickNumber = 0):
#        Gamepad.__init__(self, joystickNumber)
#        self.axisNames = {
#            0:  'LEFT-X',
#            1:  'LEFT-Y',
#            2:  'RIGHT-X',
#            3:  'RIGHT-Y',
#            4:  'roll-1',
#            5:  'pitch',
#            6:  'roll-2',
#            8:  'DPAD-UP',
#            9:  'DPAD-RIGHT',
#            10: 'DPAD-DOWN',
#            11: 'DPAD-LEFT',
#            12: 'L2',
#            13: 'R2',
#            14: 'L1',
#            15: 'R1',
#            16: 'TRIANGLE',
#            17: 'CIRCLE',
#            18: 'CROSS',
#            19: 'SQUARE'
#        }
#        self.buttonNames = {
#            0:  'SELECT',
#            1:  'L3',
#            2:  'R3',
#            3:  'START',
#            4:  'DPAD-UP',
#            5:  'DPAD-RIGHT',
#            6:  'DPAD-DOWN',
#            7:  'DPAD-LEFT',
#            8:  'L2',
#            9:  'R2',
#            10: 'L1',
#            11: 'R1',
#            12: 'TRIANGLE',
#            13: 'CIRCLE',
#            14: 'CROSS',
#            15: 'SQUARE',
#            16: 'PS'
#        }
#        self._setupReverseMaps()


class PS4(Gamepad):
    fullName = 'PlayStation 4 controller'

    def __init__(self, joystickNumber = 0):
        Gamepad.__init__(self, joystickNumber)
        self.axisNames = {
            0: 'LEFT-X',
            1: 'LEFT-Y',
            2: 'L2',
            3: 'RIGHT-X',
            4: 'RIGHT-Y',
            5: 'R2',
            6: 'DPAD-X',
            7: 'DPAD-Y'
        }
        self.buttonNames = {
            0:  'CROSS',
            1:  'CIRCLE',
            2:  'TRIANGLE',
            3:  'SQUARE',
            4:  'L1',
            5:  'R1',
            6:  'L2',
            7:  'R2',
            8:  'SHARE',
            9:  'OPTIONS',
            10: 'PS',
            11: 'L3',
            12: 'R3'
        }
        self._setupReverseMaps()


# PS4 controller settings for older Raspbian versions
#class PS4(Gamepad):
#    fullName = 'PlayStation 4 controller'
#
#    def __init__(self, joystickNumber = 0):
#        Gamepad.__init__(self, joystickNumber)
#        self.axisNames = {
#            0: 'LEFT-X',
#            1: 'LEFT-Y',
#            2: 'RIGHT-X',
#            3: 'L2',
#            4: 'R2',
#            5: 'RIGHT-Y',
#            6: 'DPAD-X',
#            7: 'DPAD-Y'
#        }
#        self.buttonNames = {
#            0:  'SQUARE',
#            1:  'CROSS',
#            2:  'CIRCLE',
#            3:  'TRIANGLE',
#            4:  'L1',
#            5:  'R1',
#            6:  'L2',
#            7:  'R2',
#            8:  'SHARE',
#            9:  'OPTIONS',
#            10: 'L3',
#            11: 'R3',
#            12: 'PS',
#            13: 'PAD'
#        }
#        self._setupReverseMaps()


class Xbox360(Gamepad):
    fullName = 'Xbox 360 controller'

    def __init__(self, joystickNumber = 0):
        Gamepad.__init__(self, joystickNumber)
        self.axisNames = {
            0: 'LEFT-X',
            1: 'LEFT-Y',
            2: 'LT',
            3: 'RIGHT-X',
            4: 'RIGHT-Y',
            5: 'RT'
        }
        self.buttonNames = {
            0:  'A',
            1:  'B',
            2:  'X',
            3:  'Y',
            4:  'LB',
            5:  'RB',
            6:  'BACK',
            7:  'START',
            8:  'XBOX',
            9:  'LA',
            10: 'RA'
        }
        self._setupReverseMaps()


class MMP1251(Gamepad):
    fullName = "ModMyPi Raspberry Pi Wireless USB Gamepad"

    def __init__(self, joystickNumber = 0):
        Gamepad.__init__(self, joystickNumber)
        self.axisNames = {
            0: 'LEFT-X',
            1: 'LEFT-Y',
            2: 'L2',
            3: 'RIGHT-X',
            4: 'RIGHT-Y',
            5: 'R2',
            6: 'DPAD-X',
            7: 'DPAD-Y'
        }
        self.buttonNames = {
            0:  'A',
            1:  'B',
            2:  'X',
            3:  'Y',
            4:  'L1',
            5:  'R1',
            6:  'SELECT',
            7:  'START',
            8:  'HOME',
            9:  'L3',
            10: 'R3'
        }
        self._setupReverseMaps()


class example(Gamepad):
    # This class must have self.axisNames with a map
    # of numbers to capitalised strings. Follow the
    # conventions the other classes use for generic
    # axes, make up your own names for axes unique
    # to your device.
    # self.buttonNames needs the same treatment.
    # Use python Gamepad.py to get the event mappings.
    fullName = 'Enter the human readable name of the device here'

    def __init__(self, joystickNumber = 0):
        Gamepad.__init__(self, joystickNumber)
        self.axisNames = {
            0: 'AXIS0',
            1: 'AXIS1',
            2: 'AXIS2'
        }
        self.buttonNames = {
            0: 'BUTTON0',
            1: 'BUTTON1',
            2: 'BUTTON2'
        }
        self._setupReverseMaps()
