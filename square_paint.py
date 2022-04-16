import cv2

img = cv2.imread('cat.jpg')     #画像の読み込み
#img = cv2.resize(img,(400,300))
cv2.rectangle(img,(120,220),(270,260),(20,20,20),-1)    #引数：(左上座標),(右下座標),(BGR値)   -1にすると塗りつぶし
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()