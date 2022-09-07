import cv2
import numpy as np
 
# create an overlay image. You can use any image
foreground = np.ones((100,100,3),dtype='uint8')*255
# Open the camera
cap = cv2.VideoCapture('./data/vtest.avi')
# Set initial value of weights
alpha = 0.4
while True:
    # read the background
    ret, background = cap.read()
    background = cv2.flip(background,1)
    # Select the region in the background where we want to add the image and add the images using cv2.addWeighted()
    imageFile = './data/lena.jpg'
    img  = cv2.imread(imageFile)  
    resize_img = cv2.resize(img, (100, 100))
    added_image = cv2.addWeighted(resize_img,alpha,background[100:200,100:200],1-alpha,0)
    # Change the region with the result
    background[100:200,100:200] = added_image
    # For displaying current value of alpha(weights)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(background,'alpha:{}'.format(alpha),(10,30), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.imshow('a',background)
    k = cv2.waitKey(10)
    # Press q to breakq
    if k == ord('q'):
        break
    # press a to increase alpha by 0.1
    if k == ord('a'):
        alpha +=0.1
        if alpha >=1.0:
            alpha = 1.0
    # press d to decrease alpha by 0.1
    elif k== ord('d'):
        alpha -= 0.1
        if alpha <=0.0:
            alpha = 0.0
# Release the camera and destroy all windows         
cap.release()
cv2.destroyAllWindows()