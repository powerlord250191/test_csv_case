from dataclasses import dataclass


@dataclass
class VideoData:
    """
    Модель данных видео с YouTube.

    Этот класс представляет собой структуру данных для хранения
    метрик видео с платформы YouTube.

    Attributes:
        title: Название видео
        ctr: Click-through rate (кликабельность) в процентах
        retention_rate: Удержание аудитории в процентах
        views: Количество просмотров
        likes: Количество лайков
        avg_watch_time: Среднее время просмотра в минутах
    """

    title: str
    ctr: float
    retention_rate: int
    views: int
    likes: int
    avg_watch_time: float

    @classmethod
    def from_csv_row(cls, row) -> "VideoData":
        """
        Создаёт экземпляр VideoData из строки CSV файла.

        Этот метод преобразует словарь, полученный при чтении CSV,
        в объект VideoData с правильными типами данных.
        """

        return cls(
            title=row["title"],
            ctr=float(row["ctr"]),
            retention_rate=int(row["retention_rate"]),
            views=int(row["views"]),
            likes=int(row["likes"]),
            avg_watch_time=float(row["avg_watch_time"]),
        )
