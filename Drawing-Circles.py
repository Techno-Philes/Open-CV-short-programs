import cv2
import numpy as np
def circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),50,(0,255,0),-1)
        
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow(winname='Cick to make circle')
cv2.setMouseCallback('Cick to make circle',circle)

while True:
    cv2.imshow('Cick to make circle',img)
    if cv2.waitKey(20) & 0xFF == 27: #ESC to exit
        break
cv2.destroyAllWindows()
