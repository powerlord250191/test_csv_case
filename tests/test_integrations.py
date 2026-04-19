from pathlib import Path
from unittest.mock import patch

import pytest

from application.main import main


@pytest.fixture
def sample_csv_path(tmp_path: Path) -> list[str]:
    test_data = """title,ctr,retention_rate,views,likes,avg_watch_time
    Нужное видео 1,15.5,35,1000,100,5.2
    Видео которое пропускаем 1,10.0,80,2000,200,8.1
    """

    test_data_2 = """title,ctr,retention_rate,views,likes,avg_watch_time
        Нужное видео 2,19.5,35,1000,100,5.2
        Видео которое пропускаем 2,14.9,39,2000,200,8.1
        """

    test_file = tmp_path / "test_data.csv"
    test_file_2 = tmp_path / "test_data_2.csv"
    test_file.write_text(test_data, encoding="utf-8")
    test_file_2.write_text(test_data_2, encoding="utf-8")

    return [str(test_file), str(test_file_2)]


def test_integrations(sample_csv_path, capsys):
    with patch(
        "sys.argv",
        [
            "application.py",
            "--files",
            sample_csv_path[0],
            sample_csv_path[1],
            "--report",
            "clickbait",
        ],
    ):
        main()

        result = capsys.readouterr()

        assert "Нужное видео 1" in result.out
        assert "Нужное видео 2" in result.out
        assert "Видео которое пропускаем 1" not in result.out
        assert "Видео которое пропускаем 2" not in result.out
