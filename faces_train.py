import cv2
print("OpenCV version:", cv2.__version__)
print("Modules available:", dir(cv2))

if hasattr(cv2, 'face'):
    print("Face module is available")
else:
    print("Face module is NOT available")