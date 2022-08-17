"""
Author          : kenl0ve
Date            : 16th Aug 2022

File            : myGPIO.py
Class           : RPI4_GPIO()
Status          : Developing Version
Description     : Initialize a GPIO object
"""

from subprocess             import call
from configuration.config   import log
from gpioConfig             import *
from utilities.singleton    import Singleton
import wiringpi

@Singleton
class GpioController():

    def __init__(self):
        # need to import the pin map and pin definitions....
        self._gpioList = {}

        call(["sudo", "chmod", "666", "/dev/mem"])
        call(["sudo", "chmod", "666", "/dev/gpiomem"])

        for pin in LIMIT_SWITCH_GPIO_CONFIGURATION:
            self._gpioList[pin['name']] = GPIO(pin)
        for pin in MOTOR_GPIO_CONFIGURATION:
            self._gpioList[pin['name']] = GPIO(pin)
        for pin in RPI_GPIO_NO_USED_CONFIGURATION:
            self._gpioList[pin['name']] = GPIO(pin)

        #ateConfig.log.logger.debug("Finished initializing GPIO pins.")

class GPIO():
    def __init__(self, pin):
        '''
        Initializes GPIO as defined in the pi4Pins dictionary.
        :param pin: Dicitonary containing pin information
        :param inferConfiguration: If true, rather than initializing the state and mode of the gpio
        to the parameters present in pin, it will load the current state.
        '''

        self.__BCM      = pin['BCM']
        self.__mode     = pin['mode']
        self.__name     = pin['name']
        self.__physical = pin['physical']
        self.__value    = pin['value']
        self.__wPi      = pin['wPi']
        self.__type     = pin['type']

        # sets wiringpi to use BCM pin numbering
        wiringpi.wiringPiSetupGpio()

        self.gpioConfig(self.__mode, self.__value)

    def gpioConfig(self, mode='out', value='0'):
        '''
        This function configures the GPIO as an input, output, or alt0.
        :param mode: String input of the desired mode.
        :return: none
        '''
        if mode in ['in', 'out', 'alt0']:
            call(["gpio", "-g", "mode", self.__BCM, mode])
            self.__mode     = mode
            self.__value    = value


            if mode == 'out':
                wiringpi.digitalWrite(int(self.__BCM), int(value))
            elif mode == 'in' and value == '0':
                call(["gpio", "-g", "mode", self.__BCM, 'down'])

            elif mode == 'in' and value == '1':
                call(["gpio", "-g", "mode", self.__BCM, 'up'])
        else:
            log.logger.error("Invalid mode for GPIO: %s" % self.__name)
            self.__mode = None

    def gpioRead(self):
        '''
        This function gets the state of the GPIO.
        :return: string value of GPIO state.
        '''

        self.__value = str(wiringpi.digitalRead(int(self.__BCM)))

        return self.__value

    def getInfo(self):
        '''
        This function returns all information pertaining to this GPIO.
        :return: Dictionary of information of this GPIO.
        '''

        # If the mode is an input, read the value in case it has been changed externally.
        if self.__mode == 'in':
            self.gpioRead()

        info =  {'BCM': self.__BCM,
                 'mode': self.__mode,
                 'name': self.__name,
                 'physical': self.__physical,
                 'value': self.__value,
                 'wPi': self.__wPi,
                }

        log.logger.debug("Info on %s: %s" % (self.__name, info))

        return info
