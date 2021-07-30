import cv2
import numpy as np

def crop(x, y, w, h, folderName) :
    
     
    img = cv2.imread(folderName + '/upload_image.png')
    roi = img[y:y+h, x:x+w] # 원본 이미지에서 선택 영영만 ROI로 지정 ---⑥
    cv2.imwrite(folderName + '/crop.png', roi)   # ROI 영역만 파일로 저장 ---⑦