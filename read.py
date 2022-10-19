import cv2 as cv #Imports cv

#Reading Images
# img = cv.imread('Photos/cat.jpg') #cv read image on folder Photos
# cv.imshow('Cat', img) #showing image('Name exibition', 'const image')
# cv.waitKey(0) #Waits for a specific delay or time in miliseconds for a key to be pressed.

#Reading Photos
capture = cv.VideoCapture('Videos/dog.mp4') #Path of dog video or use 0 to access your first camera on computer/laptop

while True: #While loop
  isTrue, frame = capture.read() #Capture to video
  cv.imshow('Dog Video', frame)

  if cv.waitKey(20) & 0xFF==ord('d'): #Run the video until it ends or D key pressed
    break

capture.release()
cv.destroyAllWindows() #Close all windows
