📄 README.md


**Gloved vs Bare Hand Detection – Part 1**



This project detects whether a hand is wearing a glove or not in images. It is designed for safety compliance use cases such as factory cameras or PPE monitoring systems.



**Dataset Name and Source**



**Dataset** **:** Gloved Hand vs Bare Hand

**Source**  **:** Roboflow Universe



The dataset contains labeled images of hands with two classes:



* gloved\_hand
* bare\_hand

&nbsp;  



The data was downloaded in YOLOv8 format and includes training, validation, and test splits.





**Model Used**



**YOLOv8 (Ultralytics)** was used for object detection.



YOLOv8 was chosen because:



* It is fast and suitable for real-time systems.
* It provides high accuracy for small objects like hands.
* It is easy to train and deploy.



The base model **yolov8n.pt** was fine-tuned on the glove dataset.





**Preprocessing and Training**



The dataset was already labeled and formatted in YOLO format.

No manual labeling was required.



Training was done using:



&nbsp;  **(yolo detect train model=yolov8n.pt data=gloved\_hand-vs-bare\_hand-2/data.yaml epochs=30 imgsz=640)**





This allowed the model to learn the difference between gloved and bare hands.

The best trained model was saved as:



&nbsp;  **(runs/detect/train2/weights/best.pt)**







**What Worked and What Didn’t**



**What worked well:**



* YOLOv8 was able to correctly detect both gloved and bare hands.
* The model performed well on clear images.
* The detection pipeline successfully produced JSON logs and annotated images.



**What didn’t work well:**



* Detection can fail when hands are very small or blurred.
* Poor lighting or occlusion can reduce accuracy.
* The dataset size is limited, so more data would improve robustness.





**How to Run the Script**



**1.** Place your input images inside:

&nbsp;    **input\_images/**



**2.** Make sure you are inside:

&nbsp;    **submission/Part\_1\_Glove\_Detection**



**3.** Run:

&nbsp;    **python detection\_script.py**





**The script will:**



* Run detection on all images.
* Save annotated images to **`output/`**
* Save detection logs to **`logs/`** in JSON format.



