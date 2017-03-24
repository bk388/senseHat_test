from ledMatrix import *
from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_imu_config(True, True, True)

CENTRE = (3, 3)
RED = [255, 0, 0]
BLUE = [0, 0, 255]

runFlag = True
sense.stick.get_events()
northAngle = 0
image = []
while runFlag:
    northAngle = sense.get_compass()
    image = getLineImage(CENTRE, northAngle+2*np.pi, 4, RED) + getLineImage(CENTRE, northAngle+np.pi, 4, BLUE)
    sense.set_pixels(image)
    if len(sense.stick.get_events()) != 0:
        runFlag = False
        
sense.clear()