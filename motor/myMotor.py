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


class Motor(models.Model):
    """A Generic class for all motors, subclassed by concrete motor type classes."""

    name = models.CharField(max_length=200, verbose_name="Human Name")
    description = models.TextField(null=True, blank=True)

    @property
    def gpio_pin_fields(self):
        """
        Return the fields of this model that contain GPIO info.

        This project is only designed to work with one RPi at a time, so pins can only
        be used once.
        Allows for checking of used GPIO pins across all motors.
        """
        raise NotImplementedError("This needs to be set by the concrete subclass.")

    def clean(self):
        """Generic model clean functions for all Motor objects."""  # noqa: D401
        super(Motor, self).clean()
        check_for_GPIO_pin_use_in_this_instance(self)
        check_for_GPIO_pin_use_in_this_and_other_models(self)

