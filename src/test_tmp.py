#from ledMatrix import *
import time
import numpy as np

lines = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
#print(draw3dVector(0, np.array([4, 4, 0]), 0))
for tick in range(10):
    print(time.time())
    time.sleep(0.5)