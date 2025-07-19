import cv2
import numpy as np


# 0 — индекс камеры (если одна камера, иначе попробуйте 1, 2 и т.д.)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Чтение кадра
    if not ret:
        print("Не удалось получить кадр!")
        break

    cv2.imshow("Webcam", frame)  # Показать кадр

image = cv2.frame


