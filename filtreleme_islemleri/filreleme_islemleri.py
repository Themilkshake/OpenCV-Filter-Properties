import cv2

import numpy as np

image=cv2.imread("filtreleme_islemleri/a.jpg")

""" 
Filtreleme işlemleri, daha çok parazitli görüntüleri daha düzgün hale getirmek içindir.

filtreleme işlemleri 3x3,4x4'lük gibi karelerle yapılır.
"""


meanfilter=cv2.blur(image,(3,3))

medianfilter=cv2.medianBlur(image,3)

gaussfilter=cv2.GaussianBlur(image,(3,3),0)


cv2.imshow("a",meanfilter)
cv2.imshow("b",medianfilter)
cv2.imshow("c",gaussfilter)

cv2.waitKey(0)
cv2.destroyAllWindows()