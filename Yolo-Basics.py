from ultralytics import YOLO
import cv2
model = YOLO("yolov8n.pt")
results = model("Images/motor.mp4", show=True)
cv2.waitKey(0)