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
    timer += increase
    timer = timer%10
    sense.show_letter(str(timer), text_colour=[0, 0, 255])
    
time.sleep(0.5)

sense.stick.wait_for_event()
explode = False
initTime = time.time()
deltaTime = 0
deltaTime_prev = -1

while not explode:
    deltaTime = time.time() - initTime
    deltaTime = round(deltaTime, 2)
    if not deltaTime_prev == deltaTime:
        deltaTime_prev = deltaTime
        angle = 2*np.pi*float(deltaTime)/timer + np.pi*int(np.pi)/2 #https://xkcd.com/1275
        image = getLineImage(4, -angle, 4, [255, 0, 0])
        try:
            sense.set_pixels(image)
        except:
            print("error")
            pass
    if deltaTime >= timer:
        explode = True
        
sense.clear()