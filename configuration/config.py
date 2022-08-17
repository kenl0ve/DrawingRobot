from utilities.myLog    import MyLog
import logging

LOG_DEBUG_MODE = False
if LOG_DEBUG_MODE == True:
    log = MyLog(logging.DEBUG)
else:
    log = MyLog(logging.INFO)


##################### X ##################### 
X_MOTOR = {
    'name'              : 'X_MOTOR', 
    'direction_gpio'    : 'GPIO18_X_MOTOR_DIRECTION',
    'pwm_gpio'          : 'GPIO27_X_MOTOR_PWM',
    'ms1_gpio'          : 'GPIO22_X_MOTOR_MS1',
    'ms2_gpio'          : 'GPIO23_X_MOTOR_MS2',
    'ms3_gpio'          : 'GPIO24_X_MOTOR_MS3'}
X_LIMIT_SWITCH_HOME = {
    'name'              : 'X_LIMIT_SWITCH_HOME', 
    'signal_gpio'       : 'GPIO2_X_LIMIT_SWITCH_HOME'}
X_LIMIT_SWITCH_END = {
    'name'              : 'X_LIMIT_SWITCH_END', 
    'signal_gpio'       : 'GPIO3_X_LIMIT_SWITCH_END'}
X_AXIS_CONFIGURATION   =   {
    'name'              : 'X_AXIS',
    'motor'             : X_MOTOR,
    'limit_switch_home' : X_LIMIT_SWITCH_HOME,
    'limit_switch_end'  : X_LIMIT_SWITCH_END}

##################### Y ##################### 
Y_MOTOR_GPIO = [ 
    {'name': 'GPIO10_Y_MOTOR_DIRECTION','type': 'pi', 'physical': '19', 'wPi': '12','BCM': '10', 'mode': 'in',   'value': '0'},
    {'name': 'GPIO9_Y_MOTOR_PWM',       'type': 'pi', 'physical': '21', 'wPi': '13','BCM': '9',  'mode': 'in',   'value': '0'},
    {'name': 'GPIO25_Y_MOTOR_MS1',      'type': 'pi', 'physical': '22', 'wPi': '6', 'BCM': '25', 'mode': 'in',   'value': '0'},
    {'name': 'GPIO11_Y_MOTOR_MS2',      'type': 'pi', 'physical': '23', 'wPi': '14','BCM': '11', 'mode': 'in',   'value': '0'},
    {'name': 'GPIO8_Y_MOTOR_MS3',       'type': 'pi', 'physical': '24', 'wPi': '10','BCM': '8',  'mode': 'in',   'value': '0'}]
Y_LIMIT_SWITCH_GPIO = [
    {'name': 'GPIO4_Y_LIMIT_SWITCH_HOME','type': 'pi', 'physical': '7',  'wPi': '7', 'BCM': '4',  'mode': 'out',  'value': '1'},
    {'name': 'GPIO14_Y_LIMIT_SWITCH_END','type': 'pi', 'physical': '8',  'wPi': '15','BCM': '14', 'mode': 'in',   'value': '0'}]

##################### Z ##################### 
Z_MOTOR_GPIOS = [ 
    {'name': 'GPIO7_Z_MOTOR_DIRECTION', 'type': 'pi', 'physical': '26', 'wPi': '11','BCM': '7',  'mode': 'in',   'value': '0'},
    {'name': 'GPIO0_Z_MOTOR_PWM',       'type': 'pi', 'physical': '27', 'wPi': '30','BCM': '0',  'mode': 'alt0', 'value': '0'},
    {'name': 'GPIO1_Z_MOTOR_MS1',       'type': 'pi', 'physical': '28', 'wPi': '31','BCM': '1',  'mode': 'alt0', 'value': '0'},
    {'name': 'GPIO5_Z_MOTOR_MS2',       'type': 'pi', 'physical': '29', 'wPi': '21','BCM': '5',  'mode': 'in',   'value': '0'},
    {'name': 'GPIO6_Z_MOTOR_MS2',       'type': 'pi', 'physical': '31', 'wPi': '22','BCM': '6',  'mode': 'in',   'value': '0'}]
Z_LIMIT_SWITCH_GPIO = [
    {'name': 'GPIO15_Z_LIMIT_SWITCH_HOME','type': 'pi', 'physical': '10', 'wPi': '16','BCM': '15', 'mode': 'in',   'value': '0'},
    {'name': 'GPIO17_Z_LIMIT_SWITCH_END', 'type': 'pi', 'physical': '11', 'wPi': '0', 'BCM': '17', 'mode': 'out',  'value': '1'}]

