import cv2

#改單點 全色
# i = cv2.imread("C:\\Users\\xd_to\\Desktop\\resource\\openCV\\02\\image\\lena256.bmp",cv2.IMREAD_UNCHANGED)
#
# print(i[123,99])
# i[123,99]=255
# print(i[123,99])


#改單點 單一色
# i = cv2.imread("C:\\Users\\xd_to\\Desktop\\resource\\openCV\\02\\image\\lenacolor.png",cv2.IMREAD_UNCHANGED)
#
# print(i[123,99])
# i[123,99,0]=255
# print(i[123,99])


#改區域
i = cv2.imread("C:\\Users\\xd_to\\Desktop\\resource\\openCV\\02\\image\\lenacolor.png",cv2.IMREAD_UNCHANGED)
cv2.imshow("original",i)
i[100:120,100:120]=[255,255,255]
cv2.imshow("result",i)
cv2.waitKey(0)
cv2.destroyAllWindows()
