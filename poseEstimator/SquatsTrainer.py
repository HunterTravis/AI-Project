import cv2
import numpy as np
import PoseModule as pm

count = 0
direction = 1

cap = cv2.VideoCapture("Videos/squats.mp4")
detector = pm.poseDetector()

while True:
    barcolor = (128, 0, 128)
    success, img = cap.read()
    #img = cv2.imread("Videos/squatspic.png")
    img = cv2.resize(img, (1280, 720))
    img = detector.findPose(img, False)

    landmarkList = detector.getPosition(img, False)

    try:
        rightAngle = detector.findAngle(img, 24, 26, 28)
        detector.drawJoints(img, 24, 26, 28, 3)
        print(rightAngle)

        # Left ARM
        leftAngle = detector.findAngle(img, 23, 25, 27)
        detector.drawJoints(img, 23, 25, 27, 3)
        print(leftAngle)

        per = np.interp((leftAngle + rightAngle) / 2, (110, 170), (100, 0))
        #
        bar = np.interp((leftAngle + rightAngle) / 2, (110, 170), (300, 650))
        #

        if per == 100:
            barcolor = (0, 255, 0)
            if direction == 1:
                count += .5
                direction = -1
        elif per == 0:
            if direction == -1:
                count += .5
                direction = 1

        #
        cv2.rectangle(img, (100, 300), (140, 650), (0, 255, 0), 2)
        cv2.rectangle(img, (100, int(bar)), (140, 650), barcolor, cv2.FILLED)
        cv2.putText(img, str(int(per)) + "%", (110, 280), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        #
        cv2.rectangle(img, (25, 20), (500, 140), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Reps:" + str(count), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)


    except:
        pass

    cv2.imshow("Image", img)
    cv2.waitKey(1)
