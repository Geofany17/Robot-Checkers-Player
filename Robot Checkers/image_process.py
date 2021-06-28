import cv2
import numpy as np
import config


def board_array(filename, state):
    '''returns array of board pieces'''
    img_size = 680 #size of final transformed board
    board = cv2.imread(filename, 1)
    assert board is not None, "eRrOr 404 FiLe nOt FoUnD"

    b_pieces = board[:, :, 0] #blue pieces of board. Will be player 1
    r_pieces = board[:, :, 2] #red pieces on board. Will be player 2
    

    cv2.imshow('blue', b_pieces)

    piece_list = [b_pieces, r_pieces]

    #corner detection
    dst = cv2.cornerHarris(b_pieces, 7, 7, 0.15)

    #filtering out found "corners" by probability it actually is a corner
    board[dst > config.corner_sensitivity * dst.max()] = [0, 0, 255]
    dst = np.argwhere(dst > config.corner_sensitivity * dst.max())

    #list of corners in format that can be passed to PerspectiveTransform
    corner_list = []
    for i in range(len(dst)):
        corner_list.append(str(dst[i])[1:-1].lstrip().split())
        corner_list[i][0], corner_list[i][1] = corner_list[i][1], corner_list[i][0]
        corner_list[i][0] = int(corner_list[i][0])
        corner_list[i][1] = int(corner_list[i][1])


    i = 0
    while i < len(corner_list) - 3: #remove all the same stuff with a while loop
        if (abs(corner_list[i][0] - corner_list[i+1][0]) < 10) or (abs(corner_list[i][1] - corner_list[i+1][1]) < 10):
            corner_list.pop(i+1)
        if (abs(corner_list[i][0] - corner_list[i+2][0]) < 10) or (abs(corner_list[i][1] - corner_list[i+2][1]) < 10):
            corner_list.pop(i+2)
        i += 1

    #preparing values for perspective transform using detected corners
    board_pts1 = np.float32([[143, 93],[494, 93],[143, 447],[497, 445]])
    board_pts2 = np.float32([[-10, -10],[685, -10],[-10, 685],[687, 687]])
    board_m = cv2.getPerspectiveTransform(board_pts1, board_pts2)

    for piece in piece_list:

        #thresholding for dark/light - to find pieces of each colour
        piece = cv2.GaussianBlur(piece, (5, 5), 0)
        
        thresh = cv2.adaptiveThreshold(piece, 250, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, config.thresh_blob_size, config.thresh_const)
        ret, thresh2 = cv2.threshold(piece, 0, 250, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        piece = cv2.addWeighted(thresh, 1, thresh2, 0.1, -.3)


    #actually carrying out the perspective transform
    r_pieces = cv2.warpPerspective(r_pieces, board_m, (img_size, img_size))
    b_pieces = cv2.warpPerspective(b_pieces, board_m, (img_size, img_size))

    #cv2.imshow('b_pieces', b_pieces)
    #cv2.imshow('r_pieces', r_pieces)
    

    #array of what piece is where
    roi_size = img_size/8

    for i in range(8):
        for j in range(8):
            state[i][j] = 0

    for row in range(8):
        a = int(row * roi_size)
        b = int((row + 1) * roi_size)
        for col in range(8):
            c = int(col * roi_size)
            d = int((col + 1) * roi_size)
            roi = b_pieces[a:b, c:d]
            if ((row + col) % 2 == 0) and (np.mean(roi) > config.blue_mean_min):
                state[row][col] = 10
            roi = r_pieces[a:b, c:d]
            if ((row + col) % 2 == 0) and (np.mean(roi) > config.red_mean_min):
                state[row][col] = 20
    
    state = state.transpose()

    for i in range(8):
        for j in range(8):
            print(state[i][j], end=' ')
        print()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return state
