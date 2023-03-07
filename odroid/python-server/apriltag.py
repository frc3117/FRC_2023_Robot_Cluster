import cv2 as cv

from threading import Thread
from pupil_apriltags import Detector


class AprilTagThread:
    def __init__(self, cap: cv.VideoCapture, detector: Detector):
        self.cap = cap
        self.detector = detector

        ret, frame = cap.read()
        if not ret:
            raise Exception("Error while reading frame from the VideoCapture")

        self.img = frame

        self.__should_run__ = False

    def start(self):
        self.__should_run__ = True

        t = Thread(target=self.__loop__, daemon=True)
        t.start()

    def stop(self):
        self.__should_run__ = False

    def __loop__(self):
        while self.__should_run__:
            ret, frame = self.cap.read()

            if ret:
                self.img = frame

    def process_results(self):
        detect_img = self.img.copy()

        gray = cv.cvtColor(detect_img, cv.COLOR_BGR2GRAY)
        return self.detector.detect(gray), detect_img
