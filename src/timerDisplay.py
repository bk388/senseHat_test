from ledMatrix import *
from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_imu_config(True, True, True)

PERIOD = 5.0

sense.stick.wait_for_event()
time.sleep(1)
end = False
initTime = time.time()
deltaTime = 0
deltaTime_prev = -1
sense.stick.get_events()
while not end:
    deltaTime = time.time() - initTime
    deltaTime = round(deltaTime, 2)%PERIOD
    if not deltaTime_prev == deltaTime:
        deltaTime_prev = deltaTime
        angle = 2*np.pi*float(deltaTime)/PERIOD + np.pi*int(np.pi)/2 #https://xkcd.com/1275
        image = getLineImage((4.5, 4.5), -angle, 4, [255, 0, 0])
        try:
            sense.set_pixels(image)
        except:
            print("error")
            pass
    if not len(sense.stick.get_events()) == 0:
        end = True
        sense.clear()
