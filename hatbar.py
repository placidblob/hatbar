import time

from sense_hat import SenseHat

class HatBar(object):

    #################################################3
    # properties

    row = 0
    length = 8
    sense = False

    _curr  = False
    min = max = False

    @property
    def curr(self):
        return self._curr

    @curr.setter
    def curr(self, val):
        self._curr = float(val)
        self.adjust_minmax()

    foreground = [0, 0, 128]
    background = [0, 0, 0]
    initcolour = [255, 255, 255]

    def __init__(self, setrow, setsense, setcol):
        self.row = setrow
        self.sense = setsense
        self.foreground = setcol

    #################################################3
    # logic

    def draw(self, value):
        self.curr = value

        if min == max:
            self.show_init()
        else:
            for i in range(0, self.length):
                self.draw_pixel(i)

    def draw_pixel(self, i):
        if self.should_be_on(i):
            # ON
            self.sense.set_pixel(i, self.row, self.foreground)
        else:
            # OFF
            self.sense.set_pixel(i, self.row, self.background)

    def show_init(self):
        # set init colour
        for i in range(0, self.length):
            self.sense.set_pixel(i, self.row, self.initcolour)

    #################################################3
    # arithmetics

    def should_be_on(self, pixel):
        # on if "pixel%" is below value
        # TODO abs here somehow
        return self.pixel2val(pixel) <= self.curr - self.min

    def adjust_minmax(self):
        if (self.min is False) or (self.curr < self.min):
            self.min = float(self.curr)
        if (self.max is False) or (self.curr > self.max):
            self.max = float(self.curr)

    def pixel2val(self, pixel):
        # if (self.max is False) or (self.min is False):
        #     return False

        range = self.max - self.min

        return (pixel + 1) * range / float(self.length)
