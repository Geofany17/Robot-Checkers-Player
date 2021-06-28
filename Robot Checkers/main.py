import json
import cv2
import config
import image_process
import checkers

path = 'C:/Users/Geofany/Pictures/Camera Roll/WIN_20210606_16_21_22_Pro.jpg'
path2 = 'C:/Users/Geofany/Pictures/Camera Roll/Test_2.jpg'
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = path 
        cv2.imwrite(img_name, frame)
        print("written!")
        config.curr_state = image_process.board_array(path, config.curr_state)
        curr_board = checkers.Checkers(config.curr_state)
        curr_board.bestMoves()

cam.release()
