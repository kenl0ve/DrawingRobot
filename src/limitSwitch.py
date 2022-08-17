from gpio.gpioController        import GpioController

LIMIT_SWITCH_IS_PRESSED         = '1'
LIMIT_SWITCH_NONE               = None

class LimitSwitch():
    _gpio_ctrl = GpioController.Instance()

    def __init__(self, kwargs=None):
        self._name                      = kwargs['name']
        self._status                    = LIMIT_SWITCH_NONE
        # GPIOs
        self._gpio                      = LimitSwitch._gpio_ctrl._gpioList[kwargs['signal_gpio']]
        
        self.init()

    def init(self):
        self._gpio.gpioConfig(mode='in')

    def read(self):
        return self._gpio.gpioRead()
    
    @property
    def is_pressed(self):
        self._status = self._gpio.gpioRead() == LIMIT_SWITCH_IS_PRESSED
        return self._status