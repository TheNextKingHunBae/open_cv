# 0203.py
import cv2
from   matplotlib import pyplot as plt

imageFile = './data/lena.jpg'
imgBGR = cv2.imread(imageFile)
plt.axis('off')






imgBGR = cv2.cvtColor(imgBGR,cv2.COLOR_BGR2RGB)
plt.imshow(imgBGR)



plt.show()
