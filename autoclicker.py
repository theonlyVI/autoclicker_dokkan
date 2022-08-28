from math import fabs
from signal import signal
from xmlrpc.client import TRANSPORT_ERROR
from zxtouch.client import zxtouch
from zxtouch.touchtypes import *
from zxtouch.toasttypes import *
import time
import signal
import sys


device = zxtouch("192.168.137.102")

# device.touch(TOUCH_DOWN, 5, 400, 400)
# device.show_toast(TOAST_MESSAGE, "this is test program", 2)
# time.sleep(1)
# print(device.get_screen_size())

# device.touch(TOUCH_DOWN, 1, 400, 1150)
# device.touch(TOUCH_UP, 1, 400, 1150)

exit = False
def main():
    """
    # For future when the crashing issues caused by ocr is fixed

    while True:
        # STA
        try:
            result = device.ocr((330, 1240, 300, 200), recognition_level=1, auto_correct=0)[1][0]["text"]
            if result == "STA O":
                real_touch(341, 1100)
                time.sleep(1)
        except IndexError:
            pass

        # Start
        try:
            result = device.ocr((630, 1550, 150, 50), recognition_level=0, auto_correct=0)[1][0]["text"]
            if result == "Start!":
                real_touch(651, 1554)
        except:
            pass

        # auto battle
        try:
            result = device.ocr((405, 1569, 100, 100), recognition_level=0, auto_correct=0)[1][0]["text"]
            if result == "Battle":
                real_touch(414, 1580)
                time.sleep(10)
        except IndexError:
            pass

        # ok
        try:
            result = device.ocr((370, 1500, 100, 100), recognition_level=0, auto_correct=0)[1][0]["text"]
            if result == "OK":
                real_touch(389, 1529)
                real_touch(389, 1529)
        except IndexError: 
            pass

        # Skip friend
        try:
            result = device.ocr((270, 640, 300, 100), recognition_level=0, auto_correct=0)[1][0]["text"]
            if result == "Friend Request":
                real_touch(170, 1080)
                real_touch(389, 1529)
        except IndexError:
            pass
        
        time.sleep(1)
        """
    newStage = True
    while True:
        signal.signal(signal.SIGINT, handler)
        # sta
        if float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_9071.JPG", 0.80, 4, 1)[1]["width"]) != 0:
            real_touch(341, 1100)
        # start
        elif float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_9073.JPG", 0.80, 4, 1)[1]["width"]) != 0:
            real_touch(651, 1554)
        # auto
        elif float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_9076.JPG", 0.95, 4, 1)[1]["width"]) != 0:
            if newStage:
                real_touch(414, 1580)
                newStage = False
        # friend limit
        elif float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_9080.JPG", 0.95, 4, 1)[1]["width"]) != 0:
            real_touch(250, 1080)
            real_touch(250, 1080)
            newStage = True
        elif float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_0.PNG", 0.95, 4, 1)[1]["width"]) != 0:
            real_touch(250, 1080)
            real_touch(250, 1080)
            # real_touch(389, 1529)
            newStage = True
        # friend limit reached
        elif float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_9084.JPG", 0.95, 4, 1)[1]["width"]) != 0:
            real_touch(250, 1080)
            real_touch(250, 1080)
            newStage = True
        # ok to screen
        elif float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_9078.JPG", 0.95, 4, 1)[1]["width"]) != 0:
            real_touch(389, 1529)
            real_touch(389, 1529)
            newStage = True
        elif float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_9088.JPG", 0.95, 4, 1)[1]["width"]) != 0:
            real_touch(250, 1080)
            real_touch(250, 1080)
            newStage=True
        real_touch(50, 1700)

        

def real_touch(x: int, y: int):
    device.touch(TOUCH_DOWN, 1, x, y)
    device.touch(TOUCH_UP, 1, x, y)

def handler(sig: int, frame):
    device.disconnect()
    print("Exited with Ctrl+C")
    sys.exit(0)

if __name__ == "__main__":
    main()