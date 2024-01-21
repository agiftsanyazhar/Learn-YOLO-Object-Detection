import cv2

# Path of Video
vidcap = cv2.VideoCapture("Videos/20240109_123839_tp00078.mp4")
success, image = vidcap.read()

count = 0
while vidcap.isOpened():
    success, image = vidcap.read()

    if not success:
        break

    cv2.imwrite(
        "D:/Kuliah/D4 - PENS/Proyek Akhir/Project/Footage/09-01-2024/20240109_123839_tp00078/20240107_062307_tp00019_%d.jpg"
        % count,
        image,
    )
    count += 1
