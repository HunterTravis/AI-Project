import cv2
import mediapipe as mp
import time
import math


class poseDetector:
    def __init__(self, mode=False, complexity=1, smooth=True, segmentation=False, smoothSegmentation=True,
                 detectioncon=0.5, trackingCon=0.5):
        self.mode = mode
        self.complexity = complexity
        self.smooth = smooth
        self.segmentation = segmentation
        self.smoothSegmentation = smoothSegmentation
        self.detectionCon = detectioncon
        self.trackingCon = trackingCon
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.complexity, self.smooth, self.segmentation,
                                     self.smoothSegmentation, self.detectionCon, self.trackingCon)

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)

        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

        return img

    def getPosition(self, img, draw=True):

        self.listt = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape

                cx, cy = int(lm.x * w), int(lm.y * h)
                self.listt.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 3, (255, 0, 255), cv2.FILLED)
            return self.listt

    def drawJoints(self, img, p1, p2, p3, thickness):
        x1, y1 = self.listt[p1][1:]
        x2, y2 = self.listt[p2][1:]
        x3, y3 = self.listt[p3][1:]

        cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), thickness)
        cv2.line(img, (x2, y2), (x3, y3), (255, 255, 255), thickness)

        # markers of joints
        cv2.circle(img, (x1, y1), 4, (0, 0, 250), 30, cv2.FILLED)
        cv2.circle(img, (x2, y2), 4, (0, 0, 250), 30, cv2.FILLED)
        cv2.circle(img, (x3, y3), 4, (0, 0, 250), 30, cv2.FILLED)

        # luxury circles
        cv2.circle(img, (x1, y1), 30, (128, 0, 128), 5)
        cv2.circle(img, (x2, y2), 30, (128, 0, 128), 5)
        cv2.circle(img, (x3, y3), 30, (128, 0, 128), 5)

    def findAngle(self, img, p1, p2, p3, draw=False):
        x1, y1 = self.listt[p1][1:]
        x2, y2 = self.listt[p2][1:]
        x3, y3 = self.listt[p3][1:]

        angle = int(math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2)))
        if angle > 180:
            angle = abs(angle - 360)
        elif angle < 0:
            angle = abs(angle)
        return angle