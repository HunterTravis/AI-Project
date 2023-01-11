import cv2
import numpy as np
import PoseModule as pm

rightcount = 0
rightdirection = 1

leftbarcolor = (128, 0, 128)
rightbarcolor = (128, 0, 128)

leftcount = 0
leftdirection = 1

cap = cv2.VideoCapture("Videos/bicepcurls.mp4")
detector = pm.poseDetector()

while True:
    leftbarcolor = (128, 0, 128)
    rightbarcolor = (128, 0, 128)
    success, img = cap.read()
    img = detector.findPose(img, False)

    landmarkList = detector.getPosition(img, False)

    # # Right ARM
    try:
        rightAngle = detector.findAngle(img, 12, 14, 16)
        detector.drawJoints(img, 12, 14, 16, 5)

        # Left ARM
        leftAngle = detector.findAngle(img, 11, 13, 15)
        detector.drawJoints(img, 11, 13, 15, 5)

        leftper = np.interp(leftAngle, (45, 150), (100, 0))
        rightper = np.interp(rightAngle, (45, 150), (100, 0))

        leftbar = np.interp(leftAngle, (45, 150), (300, 650))
        rightbar = np.interp(rightAngle, (45, 150), (300, 650))

        if leftper == 100:
            leftbarcolor = (0, 255, 0)
            rightbarcolor = (0, 255, 0)
            if leftdirection == 1:
                leftcount += 0.5
                leftdirection = -1
        elif leftper == 0:
            if leftdirection == -1:
                leftcount += 0.5
                leftdirection = 1

        if rightper == 100:
            if rightdirection == 1:
                rightcount += 0.5
                rightdirection = -1
        elif rightper == 0:
            if rightdirection == -1:
                rightcount += 0.5
                rightdirection = 1

        cv2.rectangle(img, (50, 300), (90, 650), (0, 255, 0), 2)
        cv2.rectangle(img, (50, int(leftbar)), (90, 650), leftbarcolor, cv2.FILLED)
        cv2.putText(img, str(int(leftper)) + "%", (30, 280), cv2.FONT_HERSHEY_PLAIN, 2,
                    (0, 255, 0), 2)

        cv2.rectangle(img, (100, 300), (140, 650), (0, 255, 0), 2)
        cv2.rectangle(img, (100, int(rightbar)), (140, 650), rightbarcolor, cv2.FILLED)
        cv2.putText(img, str(int(rightper)) + "%", (110, 280), cv2.FONT_HERSHEY_PLAIN, 2,
                    (0, 255, 0), 2)

        cv2.rectangle(img, (25, 20), (700, 140), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Reps:" + str(leftcount) + ", " + str(rightcount), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                    (255, 0, 0), 5)


    except:
        pass

    cv2.imshow("Image", img)
    cv2.waitKey(1)
