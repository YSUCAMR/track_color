import cv2
import numpy as np
import argparse
import sys

def nothing(x):
    pass

scale_factor = 0.5

cv2.namedWindow('image')

cv2.createTrackbar('HU','image',0,180,nothing)
cv2.createTrackbar('HL','image',0,180,nothing)
cv2.createTrackbar('SU','image',0,255,nothing)
cv2.createTrackbar('SL','image',0,255,nothing)
cv2.createTrackbar('VU','image',0,255,nothing)
cv2.createTrackbar('VL','image',0,255,nothing)
hu = 0
hl = 0
su = 0
sl = 0
vu = 0
vl = 0
image = cv2.imread(sys.argv[1])
height , width , layers = image.shape
width = int(scale_factor*width)
height = int(scale_factor*height)
print "resized" + str(height) + " " + str(width)
#print width, height, dim
image_show = cv2.resize(image, (width, height))
k = cv2.waitKey(1)

while(1):
    k = cv2.waitKey(0)
    if k==27:    # Esc key to stop
        break
    else:
        print "hue " + str(hu) + ", " + str(hl)
        print "saturation " + str(su) + ", " + str(sl)
        print "value " + str(vu) + ", " + str(vl)

    hu=cv2.getTrackbarPos('HU','image')
    hl=cv2.getTrackbarPos('HL','image')
    su=cv2.getTrackbarPos('SU','image')
    sl=cv2.getTrackbarPos('SL','image')
    vu=cv2.getTrackbarPos('VU','image')
    vl=cv2.getTrackbarPos('VL','image')

    hsv = cv2.cvtColor(image_show, cv2.COLOR_BGR2HSV)
    lower = np.array([hl, sl, vl])
    upper = np.array([hu, su, vu])

    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(image_show, image_show, mask=mask)
    cv2.imshow('image',res)

cv2.destroyAllWindows()


