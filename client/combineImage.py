import cv2
from PIL import Image, ImageOps, ImageFilter
import matplotlib.pyplot as plt
import numpy as np
import glob

def combineImage(x, y, w, h, folderName) :
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
    
    
    img = cv2.imread(folderName + '/upload_image.png')
    
    contents = [cv2.imread(file) for file in glob.glob(folderName + '/changeBackground/*.png')]
    
    for i, content in enumerate(contents) :
        img[y:y+h, x:x+w] = content # 원본 이미지에서 선택 영영만 ROI로 지정 ---⑥
        cv2.imwrite(folderName + '/combine/' + str(i) + '.png', img)   # ROI 영역만 파일로 저장 ---⑦
    
if __name__ == "__main__":
    combineImage(10, 10, 89, 89, '202173092', '1')