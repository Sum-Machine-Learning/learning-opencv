import cv2 as cv #Import OpenCV library

image = cv.imread('Photos/park.jpg')
cv.imshow('Boston', image) #Showing image

# Converting to grayscale
grayscale = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Gray image', grayscale) #Showing gray image

# Blur
blur = cv.GaussianBlur(image, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur image', blur) #Showing blur image

# Edge Cascade
canny = cv.Canny(image, 125, 125)
cv.imshow('Canny edges', canny) #Showing canny edges image

# Edge Cascade with blur
cannyblur = cv.Canny(blur, 125, 125)
cv.imshow('Canny edges blur', cannyblur) #Showing canny edges with blur image

# How to dilate an image using a specific structuring element
# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=1)
cv.imshow('Dilated', dilated) #Showing dilate image

#Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded) #Showing dilate image

#Resize
resized = cv.resize(image, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized) #Showing resized image

#Cropping
cropped = image[50:200, 200:400]
cv.imshow('Cropped', cropped) #Showing cropped image

cv.waitKey(0)