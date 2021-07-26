import cv2
from PIL import Image, ImageOps, ImageFilter
import matplotlib.pyplot as plt
import numpy as np

def combineImage(x, y, w, h) :
    # #--① 이미지 읽기
    # img = cv2.imread('../images/upload_image.png')
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # content = cv2.imread('../images/test3.png')
    # content = cv2.cvtColor(content, cv2.COLOR_BGR2RGB)

    # h0, w0, c = img.shape

    # content = cv2.resize(content, dsize=(w0, h0))
    
    # print(img.shape)
    # print(content.shape)

    # #--② 마스크 만들기
    # mask = np.zeros((384, 384, 3), np.uint8)
    # mask = cv2.rectangle(mask, (x, y), (w, h), (255,255,255), -1)

    # mask = cv2.bitwise_and(mask, content)

    # #--③ 마스킹
    # combine = cv2.bitwise_or(img, mask)

    
    # cv2.imwrite('../images/combine.png', combine)
    
    
    img = cv2.imread('./static/images/upload_image.png')
    
    content = cv2.imread('./static/images/changeBackground.png')
    
    img[y:y+h, x:x+w] = content # 원본 이미지에서 선택 영영만 ROI로 지정 ---⑥
    cv2.imwrite('./static/images/conbine.png', img)   # ROI 영역만 파일로 저장 ---⑦
    
if __name__ == "__main__":
    combineImage(50, 50, 121, 121)