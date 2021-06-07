import cv2
from PIL import Image, ImageOps, ImageFilter
import matplotlib.pyplot as plt
import numpy as np

def makePartOfImage() :
    img = cv2.imread('../images/test111.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    content = cv2.imread('../images/crop.png')
    content = cv2.cvtColor(content, cv2.COLOR_BGR2RGB)

    h, w, c = content.shape

    img = cv2.resize(img, dsize=(h, w))

    mark = np.copy(img)

    #  BGR 제한 값 설정
    blue_threshold = 200
    green_threshold = 200
    red_threshold = 200
    bgr_threshold = [blue_threshold, green_threshold, red_threshold]

    # BGR 제한 값보다 작으면 검은색으로
    thresholds = (img[:,:,0] < bgr_threshold[0]) \
                | (img[:,:,1] < bgr_threshold[1]) \
                | (img[:,:,2] < bgr_threshold[2])
    mark[thresholds] = [0,0,0]

    mask = cv2.bitwise_not(mark)

    img1 = cv2.bitwise_or(content, mask)

    img2 = cv2.bitwise_and(img1, img)

    img3 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    cv2.imwrite('../images/test2.png', img3)
    
if __name__ == "__main__":
    makePartOfImage()