from signal import signal
from zxtouch.client import zxtouch
from zxtouch.touchtypes import *
from zxtouch.toasttypes import *
import time


# device = zxtouch("127.0.0.1")
device = zxtouch("192.168.137.59")

def real_touch(x: int, y: int):
    device.touch(TOUCH_DOWN, 1, x, y)
    device.touch(TOUCH_UP, 1, x, y)


newStage = True
while True:
    if float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_9071.JPG", 0.80, 1, 1)[1]["width"]) != 0:
        real_touch(341, 1100)
    elif float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_9073.JPG", 0.80, 1, 1)[1]["width"]) != 0:
        real_touch(651, 1554)
    elif float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_9076.JPG", 0.95, 1, 1)[1]["width"]) != 0:
        if newStage:
            real_touch(414, 1580)
            newStage = False
    elif float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_9080.JPG", 0.95, 1, 1)[1]["width"]) != 0:
        real_touch(250, 1080)
        real_touch(250, 1080)
        newStage = True
    elif float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_0.PNG", 0.95, 1, 1)[1]["width"]) != 0:
        real_touch(250, 1080)
        real_touch(250, 1080)
        # real_touch(389, 1529)
        newStage = True
    elif float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_9084.JPG", 0.95, 1, 1)[1]["width"]) != 0:
        real_touch(250, 1080)
        real_touch(250, 1080)
        newStage = True
    elif float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_9078.JPG", 0.95, 1, 1)[1]["width"]) != 0:
        real_touch(389, 1529)
        real_touch(389, 1529)
        newStage = True
    elif float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_9088.JPG", 0.95, 1, 1)[1]["width"]) != 0:
        real_touch(250, 1080)
        real_touch(250, 1080)
        newStage=True
    elif float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_9090.JPG", 0.95, 1, 1)[1]["width"]) != 0:
        device.show_toast(TOAST_MESSAGE, "The script has been terminated.", 2)
        break
    real_touch(50, 1700)
