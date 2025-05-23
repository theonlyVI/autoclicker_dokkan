from array import array
from signal import signal
from zxtouch.client import zxtouch
from zxtouch.touchtypes import *
from zxtouch.toasttypes import *
import time
import signal
import sys


device = zxtouch("192.168.2.118")
# device = zxtouch("10.0.0.230")

# device.touch(TOUCH_DOWN, 5, 400, 400)
# device.show_toast(TOAST_MESSAGE, "this is test program", 2)
# time.sleep(1)
# print(device.get_screen_size())

# device.touch(TOUCH_DOWN, 1, 400, 1150)
# device.touch(TOUCH_UP, 1, 400, 1150)

def main():
    # print(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_9125.JPG", 0.95, 4, 1))
    # print(device.search_color((611, 1483, 200, 300), 210, 255, 220, 255, 220, 255))
    # print(device.pick_color(530, 1017))

    
    # sta
    while True:
        signal.signal(signal.SIGINT, handler)
        # sta
        if compare_color(device.pick_color(421, 1263)[1], (242, 238, 13)):
            real_touch(341, 1100)
        # start
        elif compare_color(device.pick_color(663, 1555)[1], (169, 48, 48)):
            real_touch(651, 1554)
        # auto
        elif compare_color(device.pick_color(414, 1580)[1], (194, 194, 194)):
            real_touch(414, 1580)
            time.sleep(20)
        # single ok button
        elif compare_color(device.pick_color(650, 1088)[1], (242, 150, 45)):
            real_touch(250, 1080)
        # friend limit reached
        elif compare_color(device.pick_color(384, 1102)[1], (210, 97, 15)):
            real_touch(250, 1080)
        elif compare_color(device.pick_color(230, 1580)[1], (7, 35, 80)):
            real_touch(389, 1529)
        elif compare_color(device.pick_color(705, 1663)[1], (234,67,53)):
            device.show_toast(TOAST_MESSAGE, "The program has been terminated", 2)
            device.disconnect()
            break
        real_touch(50, 1700)

def compare_color(c1: dict, c2: tuple):
    if int(c1["red"]) == c2[0] and int(c1["green"]) == c2[1]:
        return True
    return False

def real_touch(x: int, y: int):
    device.touch(TOUCH_DOWN, 1, x, y)
    device.touch(TOUCH_UP, 1, x, y)
    # time.sleep(0.5)

def handler(sig: int, frame):
    device.disconnect()
    print("\nExited with Ctrl+C")
    sys.exit(0)

if __name__ == "__main__":
    main()