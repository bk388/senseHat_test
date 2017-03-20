"""The file containing the functions used to handle the LED display"""

import numpy as np

def getPixelValue(px, centre, angle, length, intensity=1.0):
    px = np.array(px)
    centre = np.array(centre)
    px -= centre
    signX = np.sign(np.cos(angle))
    if signX == 0:
        signX = 1
    signY = np.sign(np.sin(angle))
    if signY == 0:
        signY = 1
        
    if np.all(px == 0):
        return intensity/2
    if px[0]*np.cos(angle)<0 or px[1]*np.sin(angle)<0:
        return 0
    
    unitLen = abs( 1 / max(np.cos(angle), np.sin(angle)) )
    
    x_vert_inner = px[0] - 0.5*signX
    y_vert_inner = x_vert_inner * np.tan(angle)
    
    x_vert_outer = px[0] + 0.5*signX
    y_vert_outer = x_vert_outer * np.tan(angle)
    
    y_horiz_inner = px[1] - 0.5*signY
    x_horiz_inner = y_horiz_inner/np.tan(angle)
    
    y_horiz_outer = px[1] + 0.5*signY
    x_horiz_outer = y_horiz_outer/np.tan(angle)
    """These are the coordinates of the intersection points of the line and the lines aligned on the
        horizontal/vertical boundaries of the pixel. Inner: closer boundaries, outer:further boundaries"""
    if px[0] == 0:
        x_vert_inner = x_horiz_inner
        y_vert_inner = y_horiz_inner
    if px[1] == 0:
        x_horiz_inner = x_vert_inner
        y_horiz_inner = y_vert_inner
    
    if abs(x_horiz_outer) < abs(x_vert_inner) or abs(x_vert_outer) < abs(x_horiz_inner):
        return 0
    
    x_inner = signX*max( abs(x_horiz_inner), abs(x_vert_inner) )
    x_outer = signX*min( abs(x_horiz_outer), abs(x_vert_outer), abs(length*np.cos(angle)) )
    if abs(x_outer) < abs(x_inner):
        return 0
    
    y_inner = signY*max( abs(y_horiz_inner), abs(y_vert_inner) )
    y_outer = signY*min( abs(y_horiz_outer), abs(y_vert_outer), abs(length*np.sin(angle)) )
    if abs(y_outer) < abs(y_inner):
        return 0
    #this is redundant, but I put it here to reassure myself. Also looks neater
    
    return intensity * np.linalg.norm([x_outer-x_inner, y_outer-y_inner]) / unitLen 
    #last line could have been done with (x_outer-x_inner)/cos(angle), but it wouldn't work when cos(angle) == 0

def getLineImage(centre, angle, length, colour, width=8, height=8):
    ledIntensities = np.zeros([width, height])
    for xx in range(2*int(length) + 3):
        for yy in range(2*int(length) + 3):
            if xx < 8 and yy < 8:
                ledIntensities[xx, 7-yy] = getPixelValue((xx, yy), centre, angle, length)
    
    colour = np.array(colour)
    ledValues = np.array([ledIntensities, ledIntensities, ledIntensities])
    ledValues = ledValues.T*colour
    ledValues = ledValues.astype(int)
    return ledValues.reshape(64, 3)[::-1]