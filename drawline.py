import numpy as np
import cv2

img = np.zeros((300,512,3), np.uint8)
x1 = 100
y1 = 100
x2 = 300
y2 = 300
step = 7
size = (x2-x1)/step
for i in range(0,np.int(size)):
    if i%2 !=0:
        cv2.line(img, (x1 + step * i, y1 + step * i), (x1 + step * (i + 1), y1 + +step * (i + 1)), (0, 255, 0), 3)


cv2.imshow("111",img)

cv2.waitKey()