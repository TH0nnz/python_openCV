import cv2

i = cv2.imread("C:\\Users\\xd_to\\Desktop\\resource\\openCV\\02\\image\\test.png")
cv2.imshow("Demo",i)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("C:\\Users\\xd_to\\Desktop\\resource\\openCV\\02\\image\\test2.png",i)