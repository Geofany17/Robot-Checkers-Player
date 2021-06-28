# Robot-Checkers-Player
This is the code for my Final Thesis Project about Robot playing Checkers Game. It uses Python, OpenCV, and uses a Cartesian/Gantry Robot model that operates using GRBL. The camera is placed on top for detection of boards and pieces. I used Visual Studio 2019 to write the code as well as the Arduino IDE to control the motors for each axis.

For a demo, see here:

Thank you for:

Checkers AI and Image Processing that I modified for my own use:

https://github.com/Dandoko/quba_robotic_arm/blob/master/computer-vision/checkers.py

https://github.com/Dandoko/quba_robotic_arm/blob/master/computer-vision/image_process.py


The following is a picture of the Board when detecting Pieces. Where the Red Pieces played by humans are marked with the number 20 and the Blue Pieces marked by the number 10 will be played by the AI.

<img width="794" alt="codeboard" src="https://user-images.githubusercontent.com/73238313/123595208-d89f4d00-d81a-11eb-9a97-fb3166152f81.PNG">

The following is a display of the Board using the warpPerspective method from OpenCV to detect the Board and also the detection of Pieces using the cv2.circle method combined with red and blue color detection. The code can be seen in the file Frame_Perspective.py

<img width="514" alt="Circle Finder" src="https://user-images.githubusercontent.com/73238313/123595776-814dac80-d81b-11eb-88f5-c8ba5acf8aa6.PNG">
