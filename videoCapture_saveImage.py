"""
videoCapture.py
"""
import cv2, sys
import time
import datetime

if sys.platform == "win32":
    import os, msvcrt
    msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)

    cap = cv2.VideoCapture('udp://192.168.10.1:11111')                    # 0 is for /dev/video0

while True: 
    ret, frm = cap.read()
    if ret == True:
        cv2.imshow('frm', frm)

    key = cv2.waitKey(1);
        
    if key == ord('q'):
        break
    elif key == ord('s'):
        file = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") +'.jpg'
        cv2.imwrite(file,frm)
        print(file, ' saved')

cap.release()
cv2.destroyAllWindows()

