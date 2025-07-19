import cv2


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Чтение кадра
    if not ret:
        print("Не удалось получить кадр!")
        break

    cv2.imshow("Webcam", frame)  # Показать кадр

    # Выход по нажатию 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  # Освободить камеру
cv2.destroyAllWindows()  # Закрыть окна