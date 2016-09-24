# mouseActions.py
# Description: Program defines behaviour for when user clicks and releases left mouse button
# Author: Ashutosh Mishra

import cv2

clickedPts = []

def mouseAction(event, x, y, flags, param):
    # Note how 'event' variable changes with users behaviour
    if event == cv2.EVENT_LBUTTONDOWN:
        print('You just pressed the left button')
    elif event == cv2.EVENT_LBUTTONUP:
        print('You just released the left button')

image = cv2.imread("../assets/cameraman.png")

# If user performs a mouse action, mouseAction() function is called
cv2.namedWindow("image")
cv2.setMouseCallback('image', mouseAction)

# Shows image and waits for key to be pressed
cv2.imshow('image', image)
cv2.waitKey()