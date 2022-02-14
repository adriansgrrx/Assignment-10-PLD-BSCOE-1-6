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
from pyzbar import pyzbar
from datetime import datetime

# Global variable for an empty text file where the encoding takes place
txtfile = "Contact Tracing Info.txt"

"""
pyzbar module section together with cv objects
"""
def readQRCode(frame):
    QRcode = pyzbar.decode(frame)
    for codes in QRcode:
        x, y , w, h = codes.rect
        # COstumizing the live scanner with its specific color, size and thickness
        QRtxt = codes.data.decode("utf-8")
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 3)
        # Costumizing the display font and its positioning
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, "COVID-19 CONTACT TRACING INFORMATION", (x - 65, y - 20), font, 1.0, (255, 255, 255), 2)
        # datetime object containing current date and time
        today = datetime.now()              
        cTime = today.strftime("%H:%M")        # HH/MM
        cDate = today.strftime("%B %d, %Y")    # mm/dd/YY
        # Reading text file and writing the scanned text to it.
        with open(txtfile, "w") as file:
            file.write( QRtxt + (f"\n\nDate of Registration: {cDate}\nTime of Registration: {cTime}"))
    return frame
"""
Main opencv module section
"""
def execute():
    # Turning on the camera of the computer using OpenCV
    camera = cv2.VideoCapture(0) # I use 0 value for my camera to function
    ret, frame = camera.read()
    while ret:
        ret, frame = camera.read()
        # Customization of the camera frame
        frame = readQRCode(cv2.resize(frame, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR_EXACT)) 
        cv2.imshow("QR Code Reader", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    # Releasing the camera that is turned on 
    camera.release()
    cv2.destroyAllWindows()
# Calling out the function
execute()