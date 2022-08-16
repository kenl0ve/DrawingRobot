'''
Author          : kenl0ve
Date            : 15th Aug 2022

File            : myStepper.py
Class           : MyStepper()
Status          : Developing Version
Description     : Initialize an individual step motor object, includes function:
                    - setDirection()        : set the direction             : CW or CCW
                    - getDirection()        : return the current direction  : CW or CCW

                    - ..........


basic_motor = StepperMotor(
                            driver_type     ="A4988",
                            name            ="Tester",
                            direction_gpio  =5,
                            pwm_gpio        =7,
                            ms1_gpio        =16,
                            ms2_gpio        =18,
                            ms3_gpio        =21)


'''
from myMotorDriver          import *
from myMotorConfig          import *
from myMotor                import *


class MyStepper():
    def __init__(self, kwargs=None):

        self._name                      = kwargs['name']
       
        # GPIOs
        self._direction_gpio            = kwargs['direction_gpio']
        self._pwm_gpio                  = kwargs['pwm_gpio']
        self._ms1_gpio                  = kwargs['ms1_gpio']
        self._ms2_gpio                  = kwargs['ms2_gpio']
        self._ms3_gpio                  = kwargs['ms3_gpio']

        # Motor status
        self._direction_of_rotation     = True
        self._step_type                 = 'full'
        self._driver_type               = 'A4988'

    @property
    def gpio_pin_fields(self):
        """Return the fields of this motor that contains GPIO info. """
        return [
            "direction_GPIO_pin",
            "step_GPIO_pin",
            "MS1_GPIO_pin",
            "MS2_GPIO_pin",
            "MS3_GPIO_pin",
        ]

    def clean(self):
        pass

    def move_steps(self, steps: int, log=True):
        if not self._controller:
            self._init_controller_class()

        log_info = (
            f"Moving stepper {self.name} {steps} x {self.steptype} steps "
            f"in the {self.direction_of_rotation} direction."
        )

        self._controller.motor_go(
            self._direction_of_rotation,
            self._steptype,
            steps,
            self._step_delay,
            self._verbose,
            self._init_delay,
        )
        if log:
            logging.info(log_info)

        return log_info

