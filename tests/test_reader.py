import pytest
from pathlib import Path
from application.reader_csv import CSVReader


@pytest.fixture
def sample_csv_path(tmp_path):
    test_data = """title,ctr,retention_rate,views,likes,avg_watch_time
    Тест1,15.5,35,1000,100,5.2
    Тест2,10.0,80,2000,200,8.1
    """
    test_file = tmp_path / "test_data.csv"
    test_file.write_text(test_data, encoding="utf-8")
    return str(test_file)


def test_read_file_success(sample_csv_path: Path):
    reader = CSVReader()
    videos = reader.read_file(sample_csv_path)

    assert len(videos) == 2
    assert videos[0].title == "Тест1"
    assert videos[0].ctr == 15.5
    assert videos[0].retention_rate == 35
    assert videos[1].title == "Тест2"
    assert videos[1].ctr == 10.0
    assert videos[1].retention_rate == 80


def test_read_file_not_found():
    reader = CSVReader()

    with pytest.raises(FileNotFoundError) as exc:
        reader.read_file("non_file.csv")

    assert str(exc.value) == "Файл не найден по указанному пути: non_file.csv"


def test_read_file_no_csv():
    reader = CSVReader()

    with pytest.raises(ValueError) as exc:
        reader.read_file("test_data.txt")

    assert str(exc.value) == "Неверный тип файла test_data.txt, ожидается файл с расширением '.csv'"


def test_read_empty_file(tmp_path):
    reader = CSVReader()
    test_file = tmp_path / "test_data.csv"
    test_file.write_text("", encoding="utf-8")

    with pytest.raises(ValueError) as exc:
        reader.read_file(str(test_file))

    assert "пуст" in str(exc.value).lower()