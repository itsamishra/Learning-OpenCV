# videoWriting.py
# Description: Program records and saves live webcam feed
# Author: Ashutosh Mishra

import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
fps = 10.0  # Controls the fps of the video created: todo look up optimal fps for webcam
out = cv2.VideoWriter()

success = out.open('../assets/output.mp4v',fourcc, fps, (1280,720),True)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,1)
        # write the flipped frame
        out.write(frame)
        cv2.imshow('frame',frame)

        # If user presses escape key program terminates
        userInput = cv2.waitKey(1)
        if userInput == 27:
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()