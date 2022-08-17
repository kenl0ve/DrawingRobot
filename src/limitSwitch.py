

LIMIT_SWITCH_IS_PRESSED         = '1'
LIMIT_SWITCH_NONE               = None

class LimitSwitch():
    def __init__(self, kwargs=None):
        self._name                      = kwargs['name']
        self._status                    = LIMIT_SWITCH_NONE
        # GPIOs
        self._gpio                      = kwargs['signal_gpio']
        
        self.init()

    def init(self):
        self._gpio.gpioConfig(mode='in')

    def read(self):
        self._status = self._gpio.gpioRead()
        return self._status
    
    @property
    def is_pressed(self):
        self._status = self._gpio.gpioRead() == LIMIT_SWITCH_IS_PRESSED
        return self._status