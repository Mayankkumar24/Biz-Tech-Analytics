import os
import json
import cv2
from ultralytics import YOLO

MODEL_PATH = "runs/detect/train2/weights/best.pt"
INPUT_DIR = "input_images"
OUTPUT_DIR = "output"
LOG_DIR = "logs"
CONFIDENCE = 0.25

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

model = YOLO("runs/detect/train2/weights/best.pt")

results = model.predict(source=INPUT_DIR, conf=CONFIDENCE, save=True)

for result in results:
    image_name = os.path.basename(result.path)
    detections = []

    for box in result.boxes:
        cls = int(box.cls[0])
        label = result.names[cls]
        conf = float(box.conf[0])

        x1, y1, x2, y2 = box.xyxy[0].tolist()
        bbox = [int(x1), int(y1), int(x2), int(y2)]

        detections.append({
            "label": label,
            "confidence": round(conf, 3),
            "bbox": bbox
        })

    json_data = {
        "filename": image_name,
        "detections": detections
    }

    json_path = os.path.join(LOG_DIR, image_name.replace(".jpg", ".json"))
    with open(json_path, "w") as f:
        json.dump(json_data, f, indent=4)
