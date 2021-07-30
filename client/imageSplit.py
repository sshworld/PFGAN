import cv2, numpy as np
import matplotlib.pylab as plt
import glob
from PIL import Image

from createFolder import createFolder

def imageSplit(w, h, folderName, n) :
    
    createFolder(folderName+ '/split')
    
    count = 1

    for i in range(n) :
        for j in range(n) :
            
            x = int(0 + i * h / n)
            x0 = int(h / n)
            y = int(0 + j * w / n)
            y0 = int(w / n)
            
            img = cv2.imread(folderName + '/upload_image.png')
            roi = img[x:x+x0, y:y+y0] # 원본 이미지에서 선택 영영만 ROI로 지정 ---⑥
            cv2.imwrite(folderName + '/split/split' + str(count) + '.png', roi)   # ROI 영역만 파일로 저장 ---⑦
            count += 1
            
if __name__ == "__main__":
    img = Image.open('./static/images/202173099' + '/upload_image.png')
    
    imageSplit(img.width, img.height, './static/images/202173099', 5)