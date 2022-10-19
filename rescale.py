import cv2 as cv #Imports cv

# img = cv.imread('Photos/cat.jpg') #cv read image on folder Photos
# cv.imshow('Cat', img) #showing image('Name exibition', 'const image')
# cv.waitKey(0) #Waits for a specific delay or time in miliseconds for a key to be pressed.

def rescaleFrame(frame, scale = 0.75): #Definition function
  #Images, Videos and Live Video
  width = int(frame.shape[1] * scale) #rescale shape image width
  height = int(frame.shape[0] * scale)
  dimensions = (width, height)

  return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeResolution(width, height):
  #Live video
  capture.set(3, width)
  capture.set(4, height)

#Reading Photos
capture = cv.VideoCapture('Videos/dog.mp4') #Path of dog video or use 0 to access your first camera on computer/laptop

while True: #While loop
  isTrue, frame = capture.read() #Capture to video

  frame_resize = rescaleFrame(frame, scale=.2)

  cv.imshow('Video', frame)
  cv.imshow('Video Resized', frame_resize)

  if cv.waitKey(20) & 0xFF==ord('d'): #Run the video until it ends or D key pressed
    break

capture.release()
cv.destroyAllWindows() #Close all windows
