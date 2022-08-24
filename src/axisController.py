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
import sys
import time
from src.stepper                        import Stepper
from src.limitSwitch                    import LimitSwitch
from configuration.axisConfig           import *
from src.stepperConfig                  import STEPPER_CLOCKWISE_DIRECTION, STEPPER_COUNTER_CLOCKWISE_DIRECTION
from utilities.myThread                 import MyThread
from configuration.config               import *

MSECS_5 = 0.005
# AXIS_MODE_      = True


class AxisController():
    def __init__(self, kwargs):
        self._name                  = kwargs['name']

        # Motor initialization
        self._motor_ctrl            = Stepper(kwargs['motor'])
        self._gear_ratio            = kwargs['grear_ratio']

        # Limit Switches initialization
        self._ls_home_ctrl          = LimitSwitch(kwargs['limit_switch_home'])
        self._ls_home_is_pressed    = self._ls_home_ctrl.is_pressed
        self._ls_end_ctrl           = LimitSwitch(kwargs['limit_switch_end'])
        self._ls_end_is_pressed     = self._ls_end_ctrl.is_pressed

        # Thread reading Limit switches
        self._lsReadingThread       = MyThread(1, 'Limit Switch Checking Thread', 2, self.readLSThread)
        self._lsReadingThread.start()
        # self._modeCheckThread   = MyThread(2, "Check Mode Thread", 2, self.checkMode)
        # self._modeCheckThread.start()

        # Axis Status
        self._axis_direction        = AXIS_MOVE_DEFAULT_DIRECTION
        self._axis_speed            = AXIS_SPEED_DEFAULT
        self._axis_mode             = kwargs['axis_mode_default']
        self._axis_length           = kwargs['axis_length']
        
        self._axis_move_forward_is  = STEPPER_CLOCKWISE_DIRECTION

    def mm2pulse(self, mm):
        pulses  = int((mm/self._gear_ratio)*self._motor_ctrl.step_revolution)
        return pulses
    
    # def reverseDirection(self):
    #     self._motor_ctrl.reverseDirection()
    def moveForward(self, mm=None):
        if self.limit_switch_is_pressed:
            raise NotImplementedError("GIVE LOG FILE")
            return

        if self._axis_move_forward_is == STEPPER_CLOCKWISE_DIRECTION:
            self._motor_ctrl.cwDirection()
        elif self._axis_move_forward_is == STEPPER_COUNTER_CLOCKWISE_DIRECTION:
            self._motor_ctrl.ccwDirection()
        
        if mm == None:
            self._motor_ctrl.move()
            raise NotImplementedError("Implement running without mm, but need to check the maximum distance")
        else:
            self._motor_ctrl.move(self.mm2pulse(mm))

    def moveForback(self, mm=None):
        if self.limit_switch_is_pressed:
            raise NotImplementedError("GIVE LOG FILE")
            return

        if self._axis_move_forward_is == STEPPER_CLOCKWISE_DIRECTION:
            self._motor_ctrl.ccwDirection()
        elif self._axis_move_forward_is == STEPPER_COUNTER_CLOCKWISE_DIRECTION:
            self._motor_ctrl.cwDirection()
        
        if mm == None:
            self._motor_ctrl.move()
            raise NotImplementedError("Implement running without mm, but need to check the maximum distance")
        else:
            self._motor_ctrl.move(self.mm2pulse(mm))

    def stop(self):
        self._motor_ctrl.stop()
    
    def findDirection(self):
        self._axis_move_forward_is = STEPPER_CLOCKWISE_DIRECTION
        distance_check_limit_switch= 1 # mm

        if self._ls_home_is_pressed:
            for x in range(1, 3):
                self.moveForward(mm=distance_check_limit_switch)
                if not self._ls_home_ctrl.is_pressed:
                    self._axis_move_forward_is = STEPPER_CLOCKWISE_DIRECTION
                    self.moveForback(mm=distance_check_limit_switch*x)
                    return
            self._axis_move_forward_is = STEPPER_COUNTER_CLOCKWISE_DIRECTION
            for x in range(1,4):
                self.moveForward(mm=distance_check_limit_switch)
                if not self._ls_home_ctrl.is_pressed:
                    self._axis_move_forward_is = STEPPER_CLOCKWISE_DIRECTION
                    self.moveForback(mm=distance_check_limit_switch*x)
                    return
            self.stop()
            raise NotImplementedError("Failure case. Cannot find Direction")
        elif self._ls_end_is_pressed:
            for x in range(1, 3):
                self.moveForback(mm=distance_check_limit_switch)
                if not self._ls_home_ctrl.is_pressed:
                    self._axis_move_forward_is = STEPPER_CLOCKWISE_DIRECTION
                    self.moveForward(mm=distance_check_limit_switch*x)
                    return
            self._axis_move_forward_is = STEPPER_COUNTER_CLOCKWISE_DIRECTION
            for x in range(1,4):
                self.moveForback(mm=distance_check_limit_switch)
                if not self._ls_home_ctrl.is_pressed:
                    self._axis_move_forward_is = STEPPER_CLOCKWISE_DIRECTION
                    self.moveForward(mm=distance_check_limit_switch*x)
                    return
            self.stop()
            raise NotImplementedError("Failure case. Cannot find Direction")
        else:
            self.moveForback()
            if self._ls_end_ctrl.is_pressed:
                self._axis_move_forward_is = STEPPER_COUNTER_CLOCKWISE_DIRECTION
            elif self._ls_home_ctrl.is_pressed:
                self._axis_move_forward_is = STEPPER_CLOCKWISE_DIRECTION
            else:
                raise NotImplementedError("Motor is stop, but no limit-switch detected")
        self.stop()

    def readLSThread(self):
        while True:
            time.sleep(MSECS_5)
            self._ls_home_is_pressed    = self._ls_home_ctrl.is_pressed
            self._ls_end_is_pressed     = self._ls_end_ctrl.is_pressed

            if self._ls_home_is_pressed or self._ls_end_is_pressed:
                self.stop()
            
    def limit_switch_home_is_pressed(self):
        return self._ls_home_ctrl.is_pressed
    def limit_switch_end_is_pressed(self):
        return self._ls_end_ctrl.is_pressed
    def rth(self):
        pass

    def find_home(self):
        self._motor_ctrl.move()

    def updateMotors(self):
        # self._motor_ctrl.save(_motor_direction, _step_type, _step_delay)
        pass
    
    def initMotor(self):
        self._motor_ctrl.init()
    

    @property
    def axis_direction(self):
        return self._axis_direction
    @axis_direction.setter
    def axis_direction(self, direction):
        self._axis_direction = direction
    
    @property
    def axis_speed(self):
        return self._axis_speed
    @axis_speed.setter
    def axis_speed(self, speed):
        self._axis_speed = speed

    @property
    def axis_mode(self):
        return self._axis_mode
    @axis_mode.setter
    def axis_mode(self, mode):
        self._axis_mode = mode

    @property
    def limit_switch_is_pressed(self):
        return self._ls_home_ctrl & self._ls_end_ctrl
