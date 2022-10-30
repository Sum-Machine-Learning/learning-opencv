#Import libs
import cv2 as cv
import numpy as np

image = cv.imread('Photos/park.jpg')
cv.imshow('Boston', image) #Showing image

# Translation
def translate(image, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (image.shape[1], image.shape[0])
    return cv.warpAffine(image, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(image, -100, 100)
cv.imshow('Translated', translated) #Showing translated image

#Rotation
def rotate(image, angle, rotPoint=None):
    (height, width) = image.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(image, rotMat, dimensions)

rotated = rotate(image, -45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, -90)
cv.imshow('Rotated Rotated', rotated_rotated)

#Resizing
resized = cv.resize(image, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#Flipping
flip = cv.flip(image, 0) #0 - 180° or 1 - mirror
cv.imshow('Flip', flip)

#Cropping
cropped = image[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)