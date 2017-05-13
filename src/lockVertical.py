from ledMatrix import *
from sense_hat import SenseHat
import time

def main():
    sense = SenseHat()
    sense.set_imu_config(True, True, True)
    
    vertVect = np.array([0.0, 0.0, 5.0])
    
    sense.set_pixels(draw3dVector([4, 4], vertVect, [255, 0, 0]))
    sense.stick.get_events()
    
    while len(sense.stick.get_events()) == 0:
        orientation = sense.get_orientation_radians()
        
        yaw = orientation["yaw"]
        pitch = orientation["pitch"]
        roll = orientation["roll"]
        rotMatrix = getRotMat(yaw, pitch, roll)
        
        vec2draw = vertVect.dot(rotMatrix)
        
        print(vec2draw)
        time.sleep(2)
        
    sense.clear()
    
main()
        
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
