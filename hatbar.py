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
        """
        Renders the bar.
        """

        # set the value (this adjusts minmax)
        self.curr = value

        if min == max:
            # not enough input yet
            self.show_init()
        else:
            # loop through the bars and draw each one
            for i in range(0, self.length):
                self.draw_pixel(i)

    def draw_pixel(self, i):
        """
        Draws a single led (pixel)
        :param i: led number. shoud ensure that  i < length
        """
        if self.should_be_on(i):
            # ON
            self.sense.set_pixel(i, self.row, self.foreground)
        else:
            # OFF
            self.sense.set_pixel(i, self.row, self.background)

    def show_init(self):
        # no input values, or all inputt is the same:
        # set "init colour"
        # !!! seeing init_colour *probably* means that there's some problem with the input !!!
        #     there is a problem with t
        for i in range(0, self.length):
            self.sense.set_pixel(i, self.row, self.initcolour)

    #################################################3
    # arithmetics

    def should_be_on(self, pixel):
        """
        Determines if given pixel should be on

        :param pixel: starts with 0
        :return: True if the passed pixel should be on
        """

        # convert LED no to percentage
        pixelval = self.pixel2val(pixel)

        # True if the current percentage is above the percentage that this pixel represents
        return pixelval <= self.curr_in_range()

    def curr_in_range(self):
        """
        :return: what self.curr would be if self.min was 0
        """

        # TODO implement logarithmic/exponential (inertial?) here

        # offset for min
        return self.curr - self.min

    def adjust_minmax(self):
        """
        Checks current value, and adjusts historic min/max
        This is called by the default setter of self.curr
        """

        # TODO implement short memory here

        # if  uninitialised or if current value is LOWER than historic MIN:
        #   adjust historic MIN
        if (self.min is False) or (self.curr < self.min):
            self.min = float(self.curr)

        # check for False, i.e. not received a value yet
        # also, if our current value is HIGHER than historic MAX:
        #   adjust historic MAX
        if (self.max is False) or (self.curr > self.max):
            self.max = float(self.curr)

    def pixel2val(self, pixel):
        """
        Converts a pixel to a value.
        Used to calculate for example:
            - on an 8-pixel bar
            - pixel=1 is 12.5%
            - pixel=2 is 25%
        :param pixel: starts with 0
        :return:
        """

        range = self.max - self.min

        return (pixel + 1) * range / float(self.length)
