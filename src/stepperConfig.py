
STEPPER_DRIVER_A4988_TYPES              = "A4988"           # Only support the Driver A4988

STEPPER_FULL_STEP_TYPE                  = 'FULL'
STEPPER_HALF_STEP_TYPE                  = '1/2'
STEPPER_1_SECTION_4_STEP_TYPE           = '1/4'

STEPPER_CLOCKWISE_DIRECTION             = True
STEPPER_COUNTER_CLOCKWISE_DIRECTION     = False
STEPPER_IS_RUNNING                      = True
STEPPER_IS_STOP                         = False
STEPPER_GO                              = '1'
STEPPER_STOP                            = '0'

STEPPER_STEP_DELAY_5_MS                 = 5
STEPPER_STEP_DELAY_10_MS                = 10
STEPPER_STEP_DELAY_20_MS                = 20
STEPPER_STEP_DELAY_50_MS                = 50
STEPPER_STEP_DELAY_100_MS               = 100

STEPPER_DRIVER_A4988_MS_PIN_LIST    = {STEPPER_FULL_STEP_TYPE          : [0, 0, 0], 
                                       STEPPER_HALF_STEP_TYPE          : [0, 1, 1],
                                       STEPPER_1_SECTION_4_STEP_TYPE   : [0, 1, 0]}

STEPPER_STEP_PER_REVOLUTION         = {STEPPER_FULL_STEP_TYPE           : 1,
                                       STEPPER_HALF_STEP_TYPE           : 2,
                                       STEPPER_1_SECTION_4_STEP_TYPE    : 4}