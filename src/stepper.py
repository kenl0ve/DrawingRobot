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
import time
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

        self._is_running                = STEPPER_IS_STOP

    def pwm(self, pulses=None):
        if pulses == None: # just move, dont care the steps
            while self._is_running == STEPPER_IS_RUNNING:
                self.pwm_gpio   = STEPPER_GO
                time.sleep(self._step_delay)
                self.pwm_gpio   = STEPPER_STOP
                time.sleep(self._step_delay)
        else:
            for x in range(0, pulses):
                if self._is_running == STEPPER_IS_RUNNING:
                    self.pwm_gpio   = STEPPER_GO
                    time.sleep(self._step_delay)
                    self.pwm_gpio   = STEPPER_STOP
                    time.sleep(self._step_delay)
        self.pwm_gpio   = STEPPER_STOP
       
    # def save(self, _motor_direction=STEPPER_CLOCKWISE_DIRECTION, _step_type=STEPPER_FULL_STEP_TYPE, _step_delay=STEPPER_STEP_DELAY_100_MS):
    #     self.motor_direction    = _motor_direction     
    #     self.step_type          = _step_type
    #     self.step_delay         = _step_delay

    def move(self, pulses=None):
        self._is_running    = STEPPER_IS_RUNNING
        self.pwm(pulses)

        # if pulses == None: # just move, dont care the steps
        #     self.pwm_gpio = STEPPER_GO
        # else:
        #     self.motor_go(pulses)

    def stop(self):
        if self._is_running == STEPPER_IS_RUNNING:
            self.pwm_gpio = STEPPER_STOP
        else:
            raise NotImplementedError("GIVE LOG FILE")
        self._is_running == STEPPER_IS_STOP

    def init(self):
        self.motor_direction    = self._motor_direction
        self.step_type          = self._step_type
        self.step_delay         = self._step_delay
        self.stop()

    # def reverseDirection(self):
    #     if self._motor_direction != STEPPER_CLOCKWISE_DIRECTION:
    #         self.motor_direction = STEPPER_CLOCKWISE_DIRECTION
    #     else:
    #         self.motor_direction = STEPPER_COUNTER_CLOCKWISE_DIRECTION
    
    def setDirection(self, direction):
        self.motor_direction = direction
    def ccwDirection(self):
        self.motor_direction = STEPPER_COUNTER_CLOCKWISE_DIRECTION
    def cwDirection(self):
        self.motor_direction = STEPPER_CLOCKWISE_DIRECTION

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
    @property
    def step_revolution(self):
        return STEPPER_STEP_PER_REVOLUTION[self.step_type]
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

    @property
    def pwm_gpio(self):
        return self._pwm_gpio
    @pwm_gpio.setter
    def pwm_gpio(self, status):
        self._pwm_gpio.gpioConfig(mode='out', value=status)

