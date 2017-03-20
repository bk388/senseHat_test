from ledMatrix import *
import time

time.sleep(1)
end = False
initTime = time.time()
deltaTime = 1
deltaTime_prev = -1
#while not end:
angle = 2*np.pi*float(deltaTime)/60.0 + np.pi
image = getLineImage(4, angle, 4, [255, 0, 0])
print(image)
print(image.shape)
for row in range(8):
    for column in range(8):
        print(image[column, row, 0], image[column, row, 1], image[column, row, 2])
#end