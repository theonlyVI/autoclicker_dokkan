from math import fabs
from signal import signal
from xmlrpc.client import TRANSPORT_ERROR
from zxtouch.client import zxtouch
from zxtouch.touchtypes import *
from zxtouch.toasttypes import *
import time
import signal
import sys
from multiprocessing import Process, Manager


# device = zxtouch("192.168.137.102")
device = zxtouch("10.0.0.230")

def real_touch(x: int, y: int):
    device.touch(TOUCH_DOWN, 1, x, y)
    device.touch(TOUCH_UP, 1, x, y)

def handler(sig: int, frame):
    device.disconnect()
    print("Exited with Ctrl+C")
    sys.exit(0)

def handler_main(sig: int, frame):
    print("Waiting for threads to exit")


def start():
    while True:
        signal.signal(signal.SIGINT, handler) 
        if float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_9071.JPG", 0.80, 4, 1)[1]["width"]) != 0: #sta
            real_touch(369, 1200)
        elif float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_9073.JPG", 0.80, 4, 1)[1]["width"]) != 0: #start
            real_touch(651, 1554)

def battle(newStage):
    while True:
        signal.signal(signal.SIGINT, handler)
        if float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_9076.JPG", 0.95, 4, 1)[1]["width"]) != 0:
            if newStage[0]:
                real_touch(414, 1580)
                newStage[0] = False
        elif float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_9080.JPG", 0.95, 4, 1)[1]["width"]) != 0:
            real_touch(250, 1080)
            real_touch(250, 1080)
            newStage[0] = True
        elif float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_0.PNG", 0.95, 4, 1)[1]["width"]) != 0:
            real_touch(250, 1080)
            real_touch(250, 1080)
            # real_touch(389, 1529)

def end(newStage):
    while True:
        # print(newStage[0])
        signal.signal(signal.SIGINT, handler)
        if float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_9084.JPG", 0.95, 4, 1)[1]["width"]) != 0:
            real_touch(250, 1080)
            real_touch(250, 1080)
            newStage[0] = True
        elif float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_9078.JPG", 0.95, 4, 1)[1]["width"]) != 0:
            real_touch(389, 1529)
            real_touch(389, 1529)
            newStage[0] = True
        elif float(device.image_match("/var/mobile/Library/ZXTouch/scripts/img/IMG_9088.JPG", 0.95, 4, 1)[1]["width"]) != 0:
            real_touch(250, 1080)
            real_touch(250, 1080)
            newStage[0] = True
        real_touch(50, 1700)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, handler_main)
    manager = Manager()
    newStage = manager.list()
    newStage.append(True)
    p1 = Process(target=start)
    p2 = Process(target=battle, args=(newStage,))
    p3 = Process(target=end, args=(newStage,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print("Processes joined successfully")
    