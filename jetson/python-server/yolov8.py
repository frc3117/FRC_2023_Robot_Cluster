from threading import Thread
from ultralytics import YOLO

class DetectionResult:
    def __init__(self, yolo_results) -> None:
        pass

class YOLOV8:
    def __init__(self, model_path:str = 'yolov8n.pt') -> None:
        self.model = YOLO(model_path)
        self.current_results: DetectionResult = None

        self._should_run = False

    def start(self):
        self._should_run = True

        t = Thread(target=self.update, daemon=False)
        t.start()

    def stop(self):
        self._should_run = False

    def update(self):
        img = None

        while self._should_run:
            self.current_results = DetectionResult(self.model([img])[0])