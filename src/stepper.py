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
from src.stepperConfig          import *
from gpio.gpioController        import GpioController

class Stepper():
    _gpio_ctrl = GpioController.Instance()

    def __init__(self, kwargs=None):
        self._name                      = kwargs['name']
       
        # GPIOs
        self._direction_gpio            = Stepper._gpio_ctrl._gpioList[kwargs['direction_gpio']]
        self._pwm_gpio                  = Stepper._gpio_ctrl._gpioList[kwargs['pwm_gpio']]
        self._ms1_gpio                  = Stepper._gpio_ctrl._gpioList[kwargs['ms1_gpio']]
        self._ms2_gpio                  = Stepper._gpio_ctrl._gpioList[kwargs['ms2_gpio']]
        self._ms3_gpio                  = Stepper._gpio_ctrl._gpioList[kwargs['ms3_gpio']]
                    
        # Motor status
        self._motor_direction           = STEPPER_CLOCKWISE_DIRECTION
        self._step_type                 = STEPPER_FULL_STEP_TYPE
        self._driver_type               = STEPPER_DRIVER_A4988_TYPES           # Hardcode A4988

        #
        self._step_delay                = STEPPER_STEP_DELAY_100_MS

    def move_steps(self, steps: int):
        '''
        Move the motors with the step stype is full step
        '''
        raise NotImplementedError("This needs to be set by the concrete subclass.")
    def move(self, direction, steps):
        if direction != self._motor_direction:
            self.reverseDirection()
        raise NotImplementedError("This needs to be set by the concrete subclass.")
    def stop(self):
        raise NotImplementedError("This needs to be set by the concrete subclass.")


    def init(self):
        self.motor_direction    = self._motor_direction
        self.step_type          = self._step_type
        self.step_delay         = self._step_delay
        self.stop()

    def reverseDirection(self):
        if self._motor_direction != STEPPER_CLOCKWISE_DIRECTION:
            self.motor_direction = STEPPER_CLOCKWISE_DIRECTION
        else:
            self.motor_direction = STEPPER_COUNTER_CLOCKWISE_DIRECTION
    
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
        if self._motor_direction == STEPPER_CLOCKWISE_DIRECTION:
            return 'clockwise'
        return 'counter-clockwise'
    @motor_direction.setter
    def motor_direction(self, direction):
        """Setter for direction of Motor."""
        if direction == STEPPER_CLOCKWISE_DIRECTION:
            self._motor_direction = STEPPER_CLOCKWISE_DIRECTION
            self._direction_gpio.gpioConfig(mode='out', value='1')
            return
        elif direction == STEPPER_COUNTER_CLOCKWISE_DIRECTION:
            self._motor_direction = STEPPER_COUNTER_CLOCKWISE_DIRECTION
            self._direction_gpio.gpioConfig(mode='out', value='0')
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
        self.ms1_gpio, self.ms2_gpio, self.ms3_gpio = STEPPER_DRIVER_A4988_MS_PIN_LIST[self._step_type]   
    
    @property
    def ms1_gpio(self):
        return self._ms1_gpio
    @ms1_gpio.setter
    def ms1_gpio(self, status):
        self._ms1_gpio.gpioConfig(mode='out', value=status)
    
    @property
    def ms2_gpio(self):
        return self._ms2_gpio
    @ms2_gpio.setter
    def ms2_gpio(self, status):
        self._ms2_gpio.gpioConfig(mode='out', value=status)
    
    @property
    def ms3_gpio(self):
        return self._ms3_gpio
    @ms3_gpio.setter
    def ms3_gpio(self, status):
        self._ms3_gpio.gpioConfig(mode='out', value=status)

