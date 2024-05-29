import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('/Users/aaronchen/Documents/GitHub/CSA_Project_Easy_Goal/Resources/Photos/park.jpg')
cv.imshow('Park', img)

# plt.imshow(img)
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('Lab', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV to BGR
lab_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV---> BGR', lab_bgr)

cv.waitKey(0)