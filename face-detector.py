import cv2
from random import randrange
#Load some pre-trained data on face frontals from opencv ()haar cascade algorithm
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#chooae an image to detect faces in
# img = cv2.imread('RDJ.jpg')   
#To capture video from webcam
webcam = cv2.VideoCapture(0)

#iterate forever over frames
while True:
    
    #Read the current frame
    successful_frame_read, frame = webcam.read()
    
    #convert image to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    
    #Draw rectangles around the face
    for (x, y, w, h) in face_coordinates:
        # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 2)
        
    #Show video frame
    cv2.imshow('The Prof', frame )
    key = cv2.waitKey(1)
    
    #Stop if the Q key is pressed
    if key==81 or key==113:
        break

"""


 

#Display the image with the face
cv2.imshow('The Prof', img)
cv2.waitKey()
 
# Check OpenCV version
# print("OpenCV version:", cv2.__version__)

# Simple test to see if the library loads correctly
# img = cv2.imread("img.jpg")  # Replace with an actual image path
# if img is None:
#     print("Image not loaded correctly!")
# else:
#     print("OpenCV is installed and working correctly!")

"""