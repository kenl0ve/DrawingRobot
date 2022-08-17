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
from stepper                import Stepper
from limitSwitch            import LimitSwitch
from utilities.myThread     import MyThread

MSECS_5 = 0.005
# AXIS_TOUCHES_END_POINT      = True


class AxisController():
    def __init__(self, kwargs):
        self._name              = kwargs['name']

        # Motor initialization
        self._motor_ctrl        = Stepper(kwargs['motor'])

        # Limit Switches initialization
        self._ls_home_ctrl      = LimitSwitch(kwargs['limit_switch_home'])
        self._ls_home_is_pressed= self._ls_home_ctrl.is_pressed
        self._ls_end_ctrl       = LimitSwitch(kwargs['limit_switch_end'])
        self._ls_end_is_pressed = self._ls_end_ctrl.is_pressed

        # Thread reading 
        self._lsReadingThread   = MyThread(1, 'Limit Switch Checking Thread', 2, self.readLSThread)
        self._lsReadingThread.start()
       
    def rth(self):
        pass
    def reverseDirection(self):
        self._motor_ctrl.reverseDirection()
    def stop(self):
        self._motor_ctrl.stop()

  
    def readLSThread(self):
        while True:
            time.sleep(MSECS_5)
            self._ls_home_is_pressed    = self._ls_home_ctrl.is_pressed
            self._ls_end_is_pressed     = self._ls_end_ctrl.is_pressed

    # def update 

    def initMotor(self):
        self._motor_ctrl.init()

def main(options):
    sys.path.append('/Users/130760/Documents/PrivateThings/Project/Drawing-Robot/source')
    from configuration.config   import X_AXIS_CONFIGURATION

    x_axis_ctrl         = AxisController(X_AXIS_CONFIGURATION)

if __name__ == "__main__":
    main(sys.argv[1:])

