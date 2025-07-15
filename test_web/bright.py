import os

label_dir = "D:/yolo_v11/dataset/valid/labels"
all_classes = set()

for filename in os.listdir(label_dir):
    if filename.endswith(".txt"):
        path = os.path.join(label_dir, filename)
        with open(path, "r") as f:
            lines = f.readlines()
            if not lines:
                print(f"ไฟล์ว่าง: {filename}")
            for line in lines:
                cls = int(line.strip().split()[0])
                all_classes.add(cls)

print("คลาสทั้งหมดที่เจอใน valid labels:", sorted(all_classes))
