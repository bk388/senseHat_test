from ledMatrix import *
from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_imu_config(True, True, True)

vertVect = np.array([0.0, 0.0, 5.0])

sense.set_pixels(draw3dVector([4, 4], vertVect, [255, 0, 0]))
sense.stick.get_events()

while len(sense.stick.get_events()) == 0:
    orientation = sense.get_orientation_radians()
    #rotYaw = np.array([[1.0, 0.0, 0.0], [0.0, np.cos(dPhi), -np.sin(dPhi)], [0.0, np.sin(dPhi), np.cos(dPhi)]])
    print(orientation["yaw"])