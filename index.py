import easyocr
from PIL import Image
import cv2
from crop import crop_image
from paddleocr import PaddleOCR
import os


# input_images_dirs = os.path.join("/home/liju/Desktop/training-data/", os.listdir('/home/liju/Desktop/training-data/'))

image_dirs = os.listdir('/home/liju/Desktop/training-data/')


num = 0

for i in range(len(image_dirs)):
    top = 965
    increment = 101
    bottom = 1065 
    input_images = os.path.join("/home/liju/Desktop/training-data/", os.listdir('/home/liju/Desktop/training-data/')[i])
    
    for j in range(9):
        num += 1
        bottom += increment
        top += increment
        crop_image(input_images, f"/home/liju/Desktop/training-data/images/image_{num}.jpg", (0, top, 1080, bottom))
    

# crop_image(input_image_path, "a.jpg", (0, 580, 100, 680))

# model = PaddleOCR(use_angle_cls=True, lang="en", ocr_version='PP-OCRv4', use_space_char=True) # need to run only once to download and load model into memory

# result = model.ocr("a.jpg", cls=True)
# for idx in range(len(result)):
#     res = result[idx]
#     for line in res:
#         singleLine = list(line[1][0])
#         print(singleLine)