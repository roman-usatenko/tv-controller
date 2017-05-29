from subprocess import call
from time import sleep

import RPi.GPIO as GPIO

PIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def is_on():
    return GPIO.input(PIN) == 0


def get_state():
    print is_on()
    return 'on' if is_on() else 'off'


def on():
    if not is_on():
        lirc('KEY_POWER')
        sleep(12)


def off():
    if is_on():
        lirc('KEY_POWER')


def do_script(script):
    on()
    for cmd in script:
        if cmd[0] == '~':
            sleep(int(cmd[1:]))
        else:
            lirc(cmd)


def cleanup():
    GPIO.cleanup()


def lirc(key):
    print key
    call(['/usr/bin/irsend', 'SEND_ONCE', 'MY_PHILIPS', key])
    sleep(0.7)
