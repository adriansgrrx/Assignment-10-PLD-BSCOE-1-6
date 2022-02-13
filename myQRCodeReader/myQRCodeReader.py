# Assignment 10

# Contact Tracing App
# 	- Create a python program that will read QRCode using your webcam
# 	- You may use any online QRCode generator to create QRCode
# 	- All personal data are in QRCode 
# 	- You may decide which personal data to include
# 	- All data read from QRCode should be stored in a text file including the date and time it was read

# Note: 
# 	- Search how to generate QRCode
# 	- Search how to read QRCode using webcam
# 	- Search how to create and write to text file
# 	- Your source code should be in github before Feb 19
# 	- Create a demo of your program (1-2 min) and send it directly to my messenger.

import cv2

def execute():
    # Turning on the camera of the computer using OpenCV
    camera = cv2.VideoCapture(0) # I use 1 value for my camera to function
    ret, frame = camera.read()
    while ret:
        ret, frame = camera.read()
        # Customization of the camera frame
        frame = cv2.resize(frame, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR_EXACT)
        cv2.imshow("QR Code Reader", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    # Releasing the camera that is turned on 
    camera.release()
    cv2.destroyAllWindows()
# Calling out the function
execute()