import cv2
import numpy as np

def main():
    
    vcap = cv2.VideoCapture("http://46.151.101.134:8082/?action=stream", cv2.CAP_FFMPEG)
    while(1):
        ret, frame = vcap.read()
        if ret is False:
            print("Frame is empty")
            break
        else:
            cv2.imshow('VIDEO', frame)
            cv2.waitKey(1)

if __name__ == '__main__':
    main()