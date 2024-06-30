import cv2
import os

mtp_path = "/run/user/1000/gvfs/mtp:host=Xiaomi_POCO_X4_Pro_5G_7e5511f4141f/Internal shared storage/DCIM/Screenshots/"

def getImage():
    dirs = sorted(os.listdir(mtp_path))

    input_image_path = os.path.join(mtp_path, dirs[-1])

    img = cv2.imread(input_image_path)

    cv2.imwrite("image/puzzle.png", img)