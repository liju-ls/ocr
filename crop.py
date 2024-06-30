import cv2
import numpy as np
import os

from PIL import Image

def crop_image(input_image_path, output_image_path, coordinates):
    image = Image.open(input_image_path)
    cropped_image = image.crop(coordinates)
    cropped_image.save(output_image_path)

def crop():
    left = 50
    right = 136
    
    top = 80
    bottom = 180

    input_image_path = os.path.join("image/", os.listdir('image/')[0])

    for i in range(9):
        
        crop_image(input_image_path, f"letters/{i}.jpg", (left, 900, right, 1900))

        left += 29 + 83
        right += 29 + 83

    img1 = cv2.imread('letters/0.jpg')
    img2 = cv2.imread('letters/1.jpg')
    img3 = cv2.imread('letters/2.jpg')
    img4 = cv2.imread('letters/3.jpg')
    img5 = cv2.imread('letters/4.jpg')
    img6 = cv2.imread('letters/5.jpg')
    img7 = cv2.imread('letters/6.jpg')
    img8 = cv2.imread('letters/7.jpg')
    img9 = cv2.imread('letters/8.jpg')

    imgMerge = np.concatenate([img1, img2, img3, img4, img5, img6, img7, img8, img9], axis=1)
    
    for i in range(9):
        crop_image("output/puzzle.jpg", f"out/{i}.jpg", (0, top, 774, bottom))
        

    cv2.imwrite("output/puzzle.jpg", imgMerge)


    word = crop_image(input_image_path, "words/words.jpg", (0, 500, 1080, 850))
