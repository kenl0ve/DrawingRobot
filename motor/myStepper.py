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
from this import d
from myMotorDriver              import *
from myStepperConfig            import *
from myMotor                    import *


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
        self._motor_direction           = STEPPER_CLOCKWISE_DIRECTION
        self._step_type                 = STEPPER_FULL_STEP_TYPE
        self._driver_type               = STEPPER_DRIVER_A4988_TYPES           # Hardcode A4988

        #
        self._step_delay                = STEPPER_STEP_DELAY_100_MS

    @property
    def gpios_info(self):
        """Return the fields of this motor that contains GPIOs info. """
        return [
            "Direction_GPIO",
            "PWM_GPIO",
            "MS1_GPIO",
            "MS2_GPIO",
            "MS3_GPIO",
        ]

    @property
    def motor_direction(self):
        if self._direction_gpio == STEPPER_CLOCKWISE_DIRECTION:
            return 'clockwise'
        return 'counter-clockwise'
    
    @motor_direction.setter
    def motor_direction(self, direction):
        """Setter for direction of Motor."""
        if direction == STEPPER_CLOCKWISE_DIRECTION:
            self._direction_gpio = STEPPER_CLOCKWISE_DIRECTION
            return
        if direction == STEPPER_COUNTER_CLOCKWISE_DIRECTION:
            self._direction_gpio = STEPPER_COUNTER_CLOCKWISE_DIRECTION
            return
        raise ValueError("Direction of Motors is not set correctly in format.")

    @property
    def step_delay(self):
        """
        Delay between steps in miliseconds.
        """
        return self._step_delay
    
    @step_delay.setter
    def step_delay(self, delay):
        """Step delay setter."""
        self._step_delay = delay
    
    @property
    def step_type(self):
        """
        Return the current step type of Motor.
        """
        return self._step_type
    
    @step_type.setter
    def step_type(self, type):
        """Step delay setter."""
        self._step_type = type
    
    

