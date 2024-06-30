#prediction of image drawn in paint
  
import joblib
import cv2
import numpy as np #pip install numpy
import time
  
model=joblib.load("model/alphabet_recognizer.ls")
  
puzzle = []

for a in range(9):
    line = []
    for b in range(9):
        im = cv2.imread(f"letters/{a}/{b}.jpg")
        im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        # im_gray  =cv2.GaussianBlur(im_gray, (15,15), 0)

        #Threshold the image
        ret, im_th = cv2.threshold(im_gray, 100, 255, cv2.THRESH_BINARY)
        im_th = cv2.bitwise_not(im_th)
        roi = cv2.resize(im_th, (102,102), interpolation  = cv2.INTER_AREA)

        rows,cols=roi.shape

        X = []

        ##  Fill the data array with pixels one by one.
        for i in range(rows):
            for j in range(cols):
                k = roi[i,j]
                if k>100:
                    k=1
                else:
                    k=0
                X.append(k)
                
        predictions = model.predict([X])
        # print("Prediction:",predictions[0])
        line.append(predictions[0])


    puzzle.append(line)

for i in puzzle:
    print(i)