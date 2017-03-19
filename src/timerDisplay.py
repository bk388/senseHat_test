from ledMatrix import *
from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_imu_config(True, True, True)

sense.stick.wait_for_event()
time.sleep(1)
end = False
initTime = time.time()
deltaTime = 0
deltaTime_prev = -1
sense.stick.get_events()
while not end:
    deltaTime = time.time() - initTime
    deltaTime = round(deltaTime, 2)%60
    if not deltaTime_prev == deltaTime:
        deltaTime_prev = deltaTime
        angle = 2*np.pi*float(deltaTime)/60.0 + np.pi
        image = getLineImage(4, angle, 4, [255, 0, 0])
        sense.set_pixels(image)
    if not len(sense.stick.get_events()) == 0:
        end = True
        sense.clear()
        