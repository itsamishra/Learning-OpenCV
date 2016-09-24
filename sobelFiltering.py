# sobelFiltering.py
# Description: Program uses Sobel filter to perform edge detection on webcam feed and displays results
# Author: Ashutosh Mishra

import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    img = cv2.cvtColor(frame, 0)
    img = cv2.flip(img, 1)

    # Display the resulting frame
    img1 = cv2.Sobel(img, 0, 1, 0)
    img2 = cv2.Sobel(img, 0, 0, 1)

    img = (img1 + img2) # todo is this correct approach? (logic: I'm combining x and y derived Sobel filter to display)

    # I can display original too to compare pcitures
    # cv2.imshow('orginal', frame)

    cv2.imshow('frame',img)


    # If user presses escape key program terminates
    userInput = cv2.waitKey(1)
    if userInput == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()