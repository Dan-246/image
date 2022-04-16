import cv2
img = cv2.imread("cat.jpg")
cv2.circle(img,(180,420),70,(0,255,255),-1)
cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()