import numpy as np

#creating the two arrays current and next position will be stored in
#blue is player 1, red is player 2
curr_state = np.array([[0 for col in range(8)] for row in range(8)])

#TO ADJUST SENSITIVITIES AS NEEDED:
red_mean_min = 100
blue_mean_min = 90
thresh_blob_size = 201
thresh_const = 5
corner_sensitivity = 0.01
