import cv2

img = cv2.imread('cat.jpg')     #画像の読み込み
#img = cv2.resize(img,(400,300))
cv2.putText(img,'Stay Home',(300,150),cv2.FONT_HERSHEY_SIMPLEX,2.0,(0,255,255),8)
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()