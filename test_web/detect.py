from ultralytics import YOLO

model = YOLO('d:/test_web/best.pt')  # ใส่ path เต็มไปเลย

results = model('d:/test_web/test/003.jpg', conf=0.05)  # ใส่ path เต็มเช่นกัน
results[0].show()
