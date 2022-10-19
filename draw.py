#Imports libs
import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8') #Blank image = default black (width x height, shape)
cv.imshow('Blank', blank)

#1. Paint the image a certain colour
# blank[200:300, 300:400] = 0,255,0
# # blank[:] = 0,0,255 #Red
# cv.imshow('Green', blank) #Exibition new blank with green color in background

#2. Draw a Rectangle
# cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=2) #thickness to borders
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1) #paint half of the canvas or the entire rectangle
# cv.imshow('Rectangle', blank)

# # 3. Draw A circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
# cv.imshow('Circle', blank)

# # 4. Draw a line
# cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
# cv.imshow('Line', blank)

#5. Write text
cv.putText(blank, 'Hello, my name is Chico', (0,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)