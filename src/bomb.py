from ledMatrix import *
from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_imu_config(True, True, True)

timer = 0

sense.show_letter(str(timer))
timer_set = False
sense.stick.get_events()
while not timer_set:
    increase = 0
    for event in sense.stick.get_events():
        if event[1] == "right" and event[2] == "pressed":
            increase += 1
        elif event[1] == "left" and event[2] == "pressed":
            increase -= 1
        elif event[1] == "middle" and event[2] == "pressed":
            timer_set = True
    sense.show_letter(str(timer))
    
time.sleep(5)
sense.clear()