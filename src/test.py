from ledMatrix import *
import time

time.sleep(1)
end = False
deltaTime = 0
angle = 2*np.pi*float(deltaTime) + np.pi/2
image = getLineImage((4, 4), angle, 4, [255, 0, 0])
image = (image.reshape(8, 8, 3).T[0] != 0).astype(int)
print(image)
print(image.shape)

deltaTime = 0.25
angle = 2*np.pi*float(deltaTime) + np.pi/2
image = getLineImage((4, 4), angle, 4, [255, 0, 0])
image = (image.reshape(8, 8, 3).T[0] != 0).astype(int)
print(image)
print(image.shape)

deltaTime = 0.5
angle = 2*np.pi*float(deltaTime) + np.pi/2
image = getLineImage((4, 4), angle, 4, [255, 0, 0])
image = (image.reshape(8, 8, 3).T[0] != 0).astype(int)
print(image)
print(image.shape)
#print(getPixelValue((, centre, angle, length, intensity))

deltaTime = 0.75
angle = 2*np.pi*float(deltaTime) + np.pi/2
image = getLineImage((4, 4), angle, 4, [255, 0, 0])
image = (image.reshape(8, 8, 3).T[0] != 0).astype(int)
print(image)
print(image.shape)

deltaTime = 0.5
angle = 2*np.pi*float(deltaTime) + np.pi/2
pixel = getPixelValue((4, 2), (4, 4), angle, 4)
print(int(pixel*255))