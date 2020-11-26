# Text segmentation
import cv2
import numpy as np

rgb = cv2.imread('../cbcc_card.png')
small = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)

#threshold the image
_, bw = cv2.threshold(small, 0.0, 255.0, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

# get horizontal mask of large size since text are horizontal components
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 1))
connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)

# find all the contours
contours, hierarchy = cv2.findContours(connected.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

#Segment the text lines
print(len(contours))
for idx in range(len(contours)):
    x, y, w, h = cv2.boundingRect(contours[idx])
    cv2.rectangle(rgb, (x, y), (x+w-1, y+h-1), (0, 255, 0), 2)