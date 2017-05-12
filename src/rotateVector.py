from ledMatrix import *
from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_imu_config(True, True, True)

lineX = np.array([5.0, 0.0, 0.0])
lineY = np.array([0.0, 5.0, 0.0])
lineZ = np.array([0.0, 0.0, 5.0])
lines = np.array([lineX, lineY, lineZ])

sense.set_pixels(draw3dVector([4, 4], lineZ, [255, 0, 0]))
sense.stick.get_events()

omega = 1.0

prevTime = time.time()
deltaTime = 0.0
"""while len(sense.stick.get_events()) == 0:
    deltaTime = time.time() - prevTime
    prevTime = prevTime + deltaTime
    dPhi = omega * deltaTime
    rotMatrix = np.array([[1.0, 0.0, 0.0], [0.0, np.cos(dPhi), -np.sin(dPhi)], [0.0, np.sin(dPhi), np.cos(dPhi)]])
    lineZ = lineZ.dot(rotMatrix)
    sense.set_pixels(draw3dVector([4, 4], lineZ, [255, 0, 0]))"""
    
end = False
while not end:
    events = sense.stick.get_events()
    deltaTime = time.time() - prevTime
    prevTime = prevTime + deltaTime
    #dPhi = omega * deltaTime
    dPhi = 0.1
    if len(events) != 0:
        for event in events:
            #print(event.direction, event.action)
            if event.direction == "middle":
                end = True
            elif event.direction == "left" and event.action == "pressed":
                #print("echo")
                #rotMatrix = np.array([[1.0, 0.0, 0.0], [0.0, np.cos(dPhi), -np.sin(dPhi)], [0.0, np.sin(dPhi), np.cos(dPhi)]])
                rotMatrix = np.array([[np.cos(dPhi), 0.0, -np.sin(dPhi)], [0.0, 1.0, 0.0], [np.sin(dPhi), 0.0, np.cos(dPhi)]])
                #lineZ = lineZ.dot(rotMatrix)
                lines = np.dot(rotMatrix, lines)
            elif event.direction == "right" and event.action == "pressed":
                rotMatrix = np.array([[np.cos(dPhi), 0.0, np.sin(dPhi)], [0.0, 1.0, 0.0], [-np.sin(dPhi), 0.0, np.cos(dPhi)]])
                #lineZ = lineZ.dot(rotMatrix)
                lines = np.dot(rotMatrix, lines)
            elif event.direction == "up" and event.action == "pressed":
                rotMatrix = np.array([[1.0, 0.0, 0.0], [0.0, np.cos(dPhi), -np.sin(dPhi)], [0.0, np.sin(dPhi), np.cos(dPhi)]])
                #lineZ = lineZ.dot(rotMatrix)
                lines = np.dot(rotMatrix, lines)
            elif event.direction == "down" and event.action == "pressed":
                rotMatrix = np.array([[1.0, 0.0, 0.0], [0.0, np.cos(dPhi), np.sin(dPhi)], [0.0, -np.sin(dPhi), np.cos(dPhi)]])
                #lineZ = lineZ.dot(rotMatrix)
                lines = np.dot(rotMatrix, lines)
        image = draw3dVector([4, 4], lines[0], [255, 0, 0]) + draw3dVector([4, 4], lines[1], [0, 255, 0]) + draw3dVector([4, 4], lineZ, [0, 0, 255])
        sense.set_pixels()
    
sense.clear()