#!/usr/bin/env python
"""
GPIO Controller Class
Created: 2017 May 30
Author: James Quen

Description:
Implementation of the GPIO controller
"""

import time
import gpio as gpio

from configuration.config   import log
from gpioConfig             import *

class GpioController():

    def __init__(self, gpioConfiguration):
        self._gpioConfiguration = gpioConfiguration

        log.logger.debug("Initializing GPIO pins.")

        for pin in self._gpioConfiguration:
            gpioList[pin['name']] = gpio.RPI4_GPIO(pin)

    def gpioInit(self):
        log.logger.debug("Do nothing")

    def set(self, pinName, mode, value):
        '''
        This function sets the GPIO high or low if it is configured as an output.
        :param pinName: The name of the pin to set.
        :param mode: The mode of the pin to set.
        :param state: String input for the desired state.
        :return: none
        '''

        gpioList[pinName].gpioConfig(mode, value)

    def configure(self, pinName, mode, value):
        '''
        This function configures the GPIO to a mode with a value
        :param pinName: The name of the pin to configure.
        :param mode: The mode of the pin to configure.
        :param value: The value of the pin to set if it is an output.
        :return: none
        '''

        gpioList[pinName].gpioConfig(mode, value)

    def read(self, pinName):
        '''
        This function gets the state of the GPIO.
        :return: string value of GPIO state.
        '''

        return str(gpioList[pinName].gpioRead())

    def poll(self, pinName, pinState, readDelay=0.1, timeout=10):
        '''
        This function polls the pin for desired pin state with a delay between reads.
        If the pin does not reach the desired state with in the time out, the function returns False.
        :param pinName: The pin usage name.
        :param pinState: The desired state of the pin.
        :param readDelay: The delay between each read.
        :param timeout: The maximum time to wait for the pin to reach desired state.
        :return: Returns True if the pin reaches desired state, otherwise returns False.
        '''

        # Error check for valid pin state.
        if str(pinState) != "1" and str(pinState) != "0":
            log.logger.error("Invalid pin state to poll. Pin state to poll must be either 1 or 0.")
            return False

        log.logger.debug("Polling %s until it is %s with a read delay of %s seconds and a timeout of %s seconds." % (pinName, str(pinState), str(readDelay), str(timeout)))
        # Get the start time.
        startTime = time.time()
        readDelay = float(readDelay)
        # Initialize variable to keep track of time.
        timePassed = 0

        # Flag to keep track of whether pin has reached desired state.
        reachedPinState = False

        # While the time passed is less than the time out, keep reading the pin.
        while timePassed <= timeout:

            # If the pin reaches the desired pin state, set flag to True and break out of loop.
            if self.read(pinName) == str(pinState):
                reachedPinState = True
                log.logger.debug("%s is %s. Break out of loop." % (pinName, str(pinState)))
                break

            # Update time passed.
            timePassed = time.time() - startTime
            log.logger.debug("Time passed while polling %s: %s seconds" % (pinName, str(timePassed)))

            # Delay between reading pin.
            time.sleep(readDelay)
        else:
            log.logger.warning("Polling %s timed out." % pinName)

        return reachedPinState, timePassed

    def getInfo(self, pinName):
        '''
        This function returns all information pertaining to this GPIO.
        :return: Dictionary of information of this GPIO.
        '''

        return gpioList[pinName].getInfo()
