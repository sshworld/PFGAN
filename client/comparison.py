import cv2, numpy as np
import matplotlib.pylab as plt
import glob

def comparison(folderName) :
    
    imgs = [cv2.imread(file) for file in glob.glob(folderName + '/combine/*.png')]
    
    imgs.append(cv2.imread(folderName + '/upload_image.png'))
    
    score = []
    
    hists = []
    for i, img in enumerate(imgs) :
        #---① 각 이미지를 HSV로 변환
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        #---② H,S 채널에 대한 히스토그램 계산
        hist = cv2.calcHist([hsv], [0,1], None, [180,256], [0,180,0, 256])
        #---③ 0~1로 정규화
        cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)
        hists.append(hist)

    query = hists[-1]
    
    methods = {'CORREL' :cv2.HISTCMP_CORREL, 'CHISQR':cv2.HISTCMP_CHISQR, 
            'INTERSECT':cv2.HISTCMP_INTERSECT,
            'BHATTACHARYYA':cv2.HISTCMP_BHATTACHARYYA}
    
    for j, (name, flag) in enumerate(methods.items()):
        print('%-10s'%name, end='\t')
        for i, (hist, img) in enumerate(zip(hists, imgs)):
            #---④ 각 메서드에 따라 img1과 각 이미지의 히스토그램 비교
            ret = cv2.compareHist(query, hist, flag)
            if flag == cv2.HISTCMP_CHISQR:
                score.append(ret)
            if flag == cv2.HISTCMP_INTERSECT: #교차 분석인 경우 
                ret = ret/np.sum(query)        #비교대상으로 나누어 1로 정규화
            print("img%d:%7.2f"% (i+1 , ret), end='\t')
        print()
        
    score.pop(-1)
    
    
    cv2.imwrite(folderName + '/combine.png', imgs[score.index(min(score))])

    
    
if __name__ == "__main__":
    comparison('202172861')