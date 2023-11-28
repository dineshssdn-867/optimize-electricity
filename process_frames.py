import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mkv', 'mov'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def process_video_persons(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'MP4V'), 24, (frame_width, frame_height))
    index = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if index%10 == 0:
            try:
                results = model.predict(frame)
            except:
                print("No error")
        try:
            cv2.rectangle(frame, (int(results[0].boxes.xyxy[0][0]), int(results[0].boxes.xyxy[0][1])), (int(results[0].boxes.xyxy[0][2]), int(results[0].boxes.xyxy[0][3])), color=(255,0,0), thickness=2)
            cv2.putText(frame, "Lights on", (50, 50), cv2.FONT_HERSHEY_SIMPLEX ,  
                    2, (255, 0, 0), 2, cv2.LINE_AA)
        except Exception as e:
            print(e)
            cv2.putText(frame, "Lights OFF", (50, 50), cv2.FONT_HERSHEY_SIMPLEX ,  
                    2, (255, 0, 0), 2, cv2.LINE_AA)

        index += 1
        out.write(frame)

    cap.release()
    out.release()