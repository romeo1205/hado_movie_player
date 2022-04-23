import json
import os
import RPi.GPIO as GPIO


os.environ.__setitem__('DISPLAY', ':0.0')


PIN_INPUT = 12
PIN_PAUSE = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_INPUT, GPIO.IN)
GPIO.setup(PIN_PAUSE, GPIO.IN)


json_open = open('MovieList.json', 'r')
json_data = json.load(json_open)
movies_num = len(json_data["movies"])


cnt = 0

ENTRY_PATH_ID = json_data["entry"]
ENTRY_PATH = json_data["movies"][ENTRY_PATH_ID]["path"]
ENTRY_PATH_NEXT = json_data["movies"][ENTRY_PATH_ID]["next"]
ENTRY_PATH_PREVIOUS = json_data["movies"][ENTRY_PATH_ID]["previous"]


path = ""
path_next = ""
path_previous = ""


try:
    while True:
        print(cnt)

except(KeyboardInterrupt, SystemExit, SystemError):
    print('exit')
    GPIO.cleanup()
