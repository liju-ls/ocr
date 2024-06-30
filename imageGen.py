import cv2
import numpy as np

img = cv2.imread("w/Ferf.png")

for i, row in enumerate(img): 
  
    for j, pixel in enumerate(img): 

        img[i][j] = [0, 0, 0] 


cv2.imwrite("w/Ferf.png", img)