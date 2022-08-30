from signal import signal
from zxtouch.client import zxtouch
from zxtouch.touchtypes import *
from zxtouch.toasttypes import *
import time
import signal
import sys


device = zxtouch("192.168.137.59")

# device.touch(TOUCH_DOWN, 5, 400, 400)
# device.show_toast(TOAST_MESSAGE, "this is test program", 2)
# time.sleep(1)
# print(device.get_screen_size())

# device.touch(TOUCH_DOWN, 1, 400, 1150)
# device.touch(TOUCH_UP, 1, 400, 1150)

device.force_stop_script_play()

device.show_toast(TOAST_MESSAGE, "The script has been stop", 2)
time.sleep(2)

device.disconnect()