import cv2 as cv

# img = cv.imread('/Users/aaronchen/Documents/GitHub/CSA_Project_Easy_Goal/aaronchen2007/Resources/Photos/cat_large.jpg')

# cv.imshow('Cat', img)

capture = cv.VideoCapture('/Users/aaronchen/Documents/GitHub/CSA_Project_Easy_Goal/aaronchen2007/Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()

cv.destroyAllWindows()