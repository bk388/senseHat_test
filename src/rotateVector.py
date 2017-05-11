from ledMatrix import *
from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_imu_config(True, True, True)

line = np.array([0.0, 0.0, 5.0])

sense.set_pixels(draw3dVector([4, 4], line, [255, 0, 0]))
sense.stick.get_events()

omega = 1.0

prevTime = time.time()
deltaTime = 0.0
"""while len(sense.stick.get_events()) == 0:
    deltaTime = time.time() - prevTime
    prevTime = prevTime + deltaTime
    dPhi = omega * deltaTime
    rotMatrix = np.array([[1.0, 0.0, 0.0], [0.0, np.cos(dPhi), -np.sin(dPhi)], [0.0, np.sin(dPhi), np.cos(dPhi)]])
    line = line.dot(rotMatrix)
    sense.set_pixels(draw3dVector([4, 4], line, [255, 0, 0]))"""
    
end = False
while not end:
    events = sense.stick.get_events()
    deltaTime = time.time() - prevTime
    prevTime = prevTime + deltaTime
    dPhi = omega * deltaTime
    if len(events) != 0:
        for event in events:
            print(event.direction, event.action)
            if event.direction == "middle":
                end = True
            """elif event.direction == "left" and event.action == "pressed":
                print("echo")
                rotMatrix = np.array([[1.0, 0.0, 0.0], [0.0, np.cos(dPhi), -np.sin(dPhi)], [0.0, np.sin(dPhi), np.cos(dPhi)]])
                line = line.dot(rotMatrix)
        sense.set_pixels(draw3dVector([4, 4], line, [255, 0, 0]))"""
    
sense.clear()