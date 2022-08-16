from log.myLog import MyLog
import logging

LOG_DEBUG_MODE = False
if LOG_DEBUG_MODE == True:
    log = MyLog(logging.DEBUG)
else:
    log = MyLog(logging.INFO)

