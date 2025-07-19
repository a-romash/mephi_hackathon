import cv2


class Camera:
    def __init__(self, camera_index=0, width=640, height=480):
        """
        Инициализация камеры.

        :param camera_index: Индекс камеры (0, 1, 2...)
        :param width: Ширина изображения
        :param height: Высота изображения
        """
        self.camera_index = camera_index
        self.width = width
        self.height = height
        self.cap = None

    def __enter__(self):
        """Контекстный менеджер для автоматического открытия/закрытия камеры."""
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Автоматическое закрытие камеры при выходе из контекста."""
        self.close()

    def open(self):
        """Открыть подключение к камере."""
        self.cap = cv2.VideoCapture(self.camera_index)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

        if not self.cap.isOpened():
            raise IOError(f"Не удалось открыть камеру с индексом {self.camera_index}")

    def close(self):
        """Закрыть подключение к камере."""
        if self.cap is not None:
            self.cap.release()
            self.cap = None

    def read(self):
        """
        Прочитать кадр с камеры.

        :return: Кортеж (success, frame), где success - bool, frame - numpy.ndarray
        """
        if self.cap is None:
            raise RuntimeError("Камера не открыта. Вызовите метод open()")

        return self.cap.read()

    def show_preview(self, window_name="Webcam", exit_key='q'):
        """
        Показать превью с камеры в реальном времени.

        :param window_name: Название окна
        :param exit_key: Клавиша для выхода (по умолчанию 'q')
        """
        try:
            while True:
                success, frame = self.read()

                if not success:
                    print("Ошибка чтения кадра!")
                    break

                cv2.imshow(window_name, frame)

                if cv2.waitKey(1) & 0xFF == ord(exit_key):
                    break
        finally:
            cv2.destroyAllWindows()

    def get_property(self, prop_id):
        """
        Получить свойство камеры.

        :param prop_id: ID свойства (например, cv2.CAP_PROP_FPS)
        :return: Значение свойства
        """
        if self.cap is None:
            raise RuntimeError("Камера не открыта. Вызовите метод open()")

        return self.cap.get(prop_id)

    def set_property(self, prop_id, value):
        """
        Установить свойство камеры.

        :param prop_id: ID свойства (например, cv2.CAP_PROP_FPS)
        :param value: Новое значение
        """
        if self.cap is None:
            raise RuntimeError("Камера не открыта. Вызовите метод open()")

        return self.cap.set(prop_id, value)