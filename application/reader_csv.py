from csv import DictReader
from pathlib import Path

from application.models import VideoData


class CSVReader:

    @staticmethod
    def read_file(file_path: str) -> list[VideoData]:
        videos = []
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"Файл не найден по указанному пути: {file_path}")

        with open(path, "r", encoding="utf-8") as file:
            reader = DictReader(file)

            for row in file:
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
