# webcam.py
# Description: Program uses OpenCV to display live webcam feed
# Author: Ashutosh Mishra

import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Flips image about y axis
    frame = cv2.flip(frame, 1)

    # Display the resulting frame
    cv2.imshow('frame',frame)

    # If user presses escape key program terminates
    userInput = cv2.waitKey(1)
    if userInput == 27:
        break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
