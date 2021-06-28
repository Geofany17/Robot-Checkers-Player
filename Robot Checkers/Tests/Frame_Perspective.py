# Importing Libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt

#Capturing video 
cap = cv2.VideoCapture(0)

while True: 
    _,frame = cap.read()
    img_size = 680
     # Plotting four circles on the video of the object you want to        see the transformation of.
    cv2.circle(frame,(143, 93),5,(0,0,255),-5)
    cv2.circle(frame, (494, 93), 5, (0, 0, 255), -1)
    cv2.circle(frame, (143, 447), 5, (0, 0, 255), -1)
    cv2.circle(frame, (497, 445), 5, (0, 0, 255), -1)    # selecting all the above four points in an array
    imgPts      = np.float32([[143, 93],[494, 93],[143, 447],[497, 445]])
    
    # selecting four points in an array for the destination video( the one you want to see as your output)
    objPoints   = np.float32([[-10, -10],[685, -10],[-10, 685],[687, 687]])    #Apply perspective transformation function of openCV2. This function will return the matrix which you can feed into warpPerspective function to get the warped image.
    matrix      = cv2.getPerspectiveTransform(imgPts,objPoints)
    result      = cv2.warpPerspective(frame, matrix, (img_size, img_size))    #Now Plotting both the videos(original, warped video)using matplotlib
    
    # ColorSpace
    hsvFrame    = cv2.cvtColor(result, cv2.COLOR_BGR2HSV)

    # Set range for red color
    red_lower = np.array([0, 114, 84], np.uint8)
    red_upper = np.array([69, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

    # Set range for blue color
    blue_lower = np.array([98, 91, 116], np.uint8)
    blue_upper = np.array([165, 255, 255], np.uint8)
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

    # For red color
    res_red = cv2.bitwise_and(result, result, 
                              mask = red_mask)

    # For blue color
    res_blue = cv2.bitwise_and(result, result,
                               mask = blue_mask)

    # Creating circle for Red Color   
    gray_img	= cv2.cvtColor(result,	cv2.COLOR_BGR2GRAY)
    img	        = cv2.medianBlur(gray_img,	5)
    cimg        = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    circles	    = cv2.HoughCircles(red_mask,cv2.HOUGH_GRADIENT, 1, 39, 
                                   param1=150, param2=10, minRadius=25, maxRadius=35)
    if circles is not None:
        circles	    = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(result, (x, y), r, (0, 0, 255), 4)
            cv2.rectangle(result, (x - 2, y - 2), (x + 1, y + 1), (0, 0, 0), -1)

    # Creating circle for Blue Color   
    gray_img	= cv2.cvtColor(result,	cv2.COLOR_BGR2GRAY)
    img	        = cv2.medianBlur(gray_img,	5)
    cimg        = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    circles	    = cv2.HoughCircles(blue_mask,cv2.HOUGH_GRADIENT, 1, 39, 
                                   param1=150, param2=10, minRadius=25, maxRadius=35)
    if circles is not None:
        circles	    = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(result, (x, y), r, (255, 0, 0), 4)
            cv2.rectangle(result, (x - 2, y - 2), (x + 1, y + 1), (0, 0, 0), -1)


    cv2.imshow('frame',frame)
    cv2.imshow('Circle Finder', result)


    if cv2.waitKey(1) & 0xff == 27:
        cv2.destroyAllWindows()
