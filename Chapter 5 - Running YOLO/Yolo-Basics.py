from ultralytics import YOLO

import cv2

model = YOLO("YOLO-Weights/yolov8l.pt")
# results = model("Chapter 5 - Running YOLO/images/1.png", show=True)
# results = model("Chapter 5 - Running YOLO/images/2.png", show=True)
results = model("Chapter 5 - Running YOLO/images/3.png", show=True)
cv2.waitKey(0)
