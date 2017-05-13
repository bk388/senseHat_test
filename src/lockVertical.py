from ledMatrix import *
from sense_hat import SenseHat
import time

def getRotMat(yaw, pitch, roll):
        yawMat = np.array([[np.cos(yaw), -np.sin(yaw), 0.0], 
                           [np.sin(yaw), np.cos(yaw), 0.0], 
                           [0.0, 0.0, 1.0]])  
        pitchMat = np.array([[np.cos(pitch), 0.0, -np.sin(pitch)], 
                             [0.0, 1.0, 0.0], 
                             [np.sin(pitch), 0.0, np.cos(pitch)]])
        rollMat = np.array([[1.0, 0.0, 0.0], 
                            [0.0, np.cos(roll), -np.sin(roll)], 
                            [0.0, np.sin(roll), np.cos(roll)]])
        
        rotationMatrix = yawMat.dot(pitchMat).dot(rollMat)
        
        return rotationMatrix
    
    
sense = SenseHat()
sense.set_imu_config(True, True, True)

#vertVect = np.array([0.0, 0.0, 5.0])
lines = np.array([[5.0, 0.0, 0.0],
                  [0.0, 5.0, 5.0],
                  [0.0, 0.0, 5.0]])

#sense.set_pixels(draw3dVector([4, 4], vertVect, [255, 0, 0]))
image = image = draw3dVector([4, 4], lines[0], [255, 0, 0]) + draw3dVector([4, 4], lines[1], [0, 255, 0]) + draw3dVector([4, 4], lines[2], [0, 0, 255])
sense.set_pixels(image)
sense.stick.get_events()

while len(sense.stick.get_events()) == 0:
    orientation = sense.get_orientation_radians()
    
    yaw = orientation["yaw"]
    pitch = orientation["pitch"]
    roll = orientation["roll"]
    rotMatrix = getRotMat(yaw, pitch, roll)
    
    """vec2draw = vertVect.dot(rotMatrix)
    vec2draw = vec2draw.dot(np.array([[-1.0, 0.0, 0.0],
                                      [0.0, 1.0, 0.0],
                                      [0.0, 0.0, 1.0]]))
    
    sense.set_pixels(draw3dVector([4, 4], vec2draw, [255, 0, 0]))"""
    lines2draw = lines.dot(rotMatrix)
    lines2draw = lines2draw.dot(np.array([[1.0, 0.0, 0.0],
                                          [0.0, -1.0, 0.0],
                                          [0.0, 0.0, 1.0]]))
    image = draw3dVector([4, 4], lines2draw[0], [255, 0, 0]) + draw3dVector([4, 4], lines2draw[1], [0, 255, 0]) + draw3dVector([4, 4], lines2draw[2], [0, 0, 255])
    sense.set_pixels(image)
    
    #print(vec2draw)
    time.sleep(0.01)
    
sense.clear()
