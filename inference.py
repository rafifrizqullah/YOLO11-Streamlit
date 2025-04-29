from ultralytics import solutions

inf = solutions.Inference(
    model="yolo11n.pt",  # you can use any model that Ultralytics support, i.e. YOLO11, or custom trained model
    
)

inf.web_ui()
# inf.inference()

# Make sure to run the file using command `streamlit run path/to/file.py`