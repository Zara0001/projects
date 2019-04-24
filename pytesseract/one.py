import cv2
import numpy as np
# from matplotlib import pyplot as plt
import argparse
import os

NUM1=110
NUM2=2

def main():

    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
            help="path to the input image")
    ap.add_argument("-r", "--NUM1", required=True,
            help="size limits to the input image range")
    ap.add_argument("-n", "--NUM2", required=True,
            help="size limits to the input image range")
    ap.add_argument("-l", "--limit", required=True,
            help="size limits to the input image range")
    args = vars(ap.parse_args())
    NUM1 = int(args["NUM1"])
    NUM2 = int(args["NUM2"])

    directory = args['image'] + '_' + args["NUM1"] + '_' + args["NUM2"] + '_' + args['limit']

    if not os.path.exists(directory):
        os.makedirs(directory)

    img = cv2.imread(args['image'],cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, None, fx = 2, fy = 2, interpolation = cv2.INTER_CUBIC)

    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,NUM1,NUM2)

    FILENAME=directory+ "//adaptiveThreshold_gaussian_" + str(NUM1) + "_" + str(NUM2) + args['image']
    cv2.imwrite(FILENAME, th3)

    FILENAME=directory + "//adaptiveThreshold_gaussian_" + str(NUM1) + "_" + str(NUM2) + "_inverted" + args['image']
    inverted = cv2.bitwise_not(th3)
    cv2.imwrite(FILENAME, inverted)

    kernel = np.ones((1,1),np.uint8)
    opening = cv2.morphologyEx(inverted, cv2.MORPH_OPEN, kernel)
    FILENAME=directory + "//adaptiveThreshold_gaussian_" + str(NUM1) + "_" + str(NUM2) + "_inverted_opening" + args['image']
    cv2.imwrite(FILENAME, opening)

    labelnum, labelimg, contours, GoCs = cv2.connectedComponentsWithStats(inverted)
    for label in range(1, labelnum):
        x,y,w,h,size = contours[label]
        if size <= int(args["limit"]):
             inverted[y:y+h, x:x+w] = 0
    FILENAME=directory + "//limit_"+args["limit"] +'_' + args['image']

    cv2.imwrite(FILENAME, inverted)

if __name__ == "__main__":
    main()
