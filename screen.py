import os


class BackLight(object):
    def __init__(self):
        self.dir = '/sys/class/gpio/gpio508'
        if not os.path.isdir(self.dir):
            with open('/sys/class/gpio/export', 'w') as bl:
                bl.write('508')
            with open(self.dir + '/direction', 'w') as bl:
                bl.write('out')
        self.on()

    def on(self):
        with open(self.dir + '/value', 'w') as bl:
            bl.write('1')

    def off(self):
        with open(self.dir + '/value', 'w') as bl:
            bl.write('0')
