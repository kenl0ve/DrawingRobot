'''
Author          : kenl0ve
Date            : 15th Aug 2022

File            : myMotor.py
Class           : MyMotor()
Status          : Developing Version
Description     : Initialize an individual step motor object, includes function:
                    - setDirection()        : set the direction             : CW or CCW
                    - getDirection()        : return the current direction  : CW or CCW

                    - ..........

'''
from myMotorDriver          import *
from myMotorConfig          import *


class MotorController():
    raise NotImplementedError("This needs to be set by the concrete subclass.")
