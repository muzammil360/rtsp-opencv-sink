import argparse
from datetime import datetime

import numpy as np
import cv2

def print_time():
    now = datetime.now()
    print(now)

def main(opts):
    address = opts.address
    delay = opts.delay 
    
    vcap = cv2.VideoCapture(address, cv2.CAP_FFMPEG)
    while(1):
        ret, frame = vcap.read()
        if ret is False:
            print("Frame is empty")
            break
        else:
            cv2.imshow('VIDEO', frame)
            cv2.waitKey(delay)
            print_time()

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--address', type=str, default='http://107.3.49.194:1024/mjpg/video.mjpg', help='camera stream address')
    parser.add_argument('--delay', type=int, default = 1000,  help='delay in milliseconds b/w two frames')
    
    args = parser.parse_args()
    print(args)


    return args

if __name__ == '__main__':
    opts = parseArgs()
    main(opts)