from csv import DictReader
from pathlib import Path

from application.models import VideoData


class CSVReader:

    @staticmethod
    def read_file(file_path: str) -> list[VideoData]:
        videos = []

        if file_path.endswith(".csv"):
            path = Path(file_path)
        else:
            raise ValueError(f"Неверный тип файла {file_path}, ожидается файл с расширением '.csv'")

        if not path.exists():
            raise FileNotFoundError(f"Файл не найден по указанному пути: {file_path}")

        if path.stat().st_size == 0:
            raise ValueError(f"Файл {file_path} пуст, выберите другой файл для анализа")

        with open(path, "r", encoding="utf-8") as file:

            lines = [line.strip() for line in file if line.strip()]

            reader = DictReader(lines)

            for row in reader:
                try:
                    data = VideoData.from_csv_row(row)
                    videos.append(data)
                except (KeyError, ValueError) as ex:
                    print(f"Во время чтения данных в строке {row} произошла ошибка - {ex}")
                    continue
        return videos

    @staticmethod
    def read_multiple_files(file_paths: list[str]):
        for row in file_paths:
            yield CSVReader.read_file(row)
