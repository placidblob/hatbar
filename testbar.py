from hatbar import HatBar

from sense_hat import SenseHat

import random
import time
import psutil

def getCPU():
    return psutil.cpu_percent()

def getRAM():
    return psutil.virtual_memory().percent


CPU_RGB = [0, 0, 128]  # light blue
CPU_BARNO = 0

RAM_RGB = [0, 128, 0]  # light green
RAM_BARNO = 1


if __name__ == "__main__":
    sense = SenseHat()
    sense.clear()


    # Initialise CPU bar
    cpubar = HatBar(CPU_BARNO, sense, CPU_RGB)
    cpubar.min = 0.0
    cpubar.max = 100.0

    # Initialise MEM bar
    membar = HatBar(RAM_BARNO, sense, RAM_RGB)
    membar.min = 0.0
    membar.max = 100.0

    yawbar = HatBar(2, sense, [64, 64, 64])
    rollbar = HatBar(3, sense, [64, 64, 64])
    pitchbar = HatBar(4, sense, [64, 64, 64])

    tempbar = HatBar(5, sense, [128, 128, 0])
    humbar = HatBar(6, sense, [64, 0, 64])
    prbar = HatBar(7, sense, [0, 128, 128])

    while(True):
        cpubar.draw(getCPU())
        membar.draw(getRAM())

        orientation = sense.get_gyroscope()

        yawbar.draw(orientation['yaw'])
        rollbar.draw(orientation['roll'])
        pitchbar.draw(orientation['pitch'])

        tempbar.draw(sense.get_temperature())
        humbar.draw(sense.get_pressure())
        prbar.draw(sense.get_humidity())

        print(cpubar.curr, membar.curr, tempbar.curr, humbar.curr, prbar.curr, sep="|")

        # Print the actual values to stdout
        # print(cpubar.curr, membar.curr, sep="|")

        # Wait
        time.sleep(.25)