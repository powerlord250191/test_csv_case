import pytest
from application.models import VideoData
from application.report_function import ClickbaitReport, ReportFactory


@pytest.fixture
def sample_videos():
    return [[
        VideoData("Test video 1", 18.2, 35, 45200, 1240, 4.2),
        VideoData("Test video 2", 22.5, 28, 128700, 3150, 3.1),
        VideoData("Test video 3", 9.5, 82, 31500, 890, 8.9)],
        [VideoData("Test video 4", 25.0, 22, 254000, 8900, 2.5),
        VideoData("Test video 5", 19.0, 38, 87600, 2100, 4.5),
    ]]


def test_clickbait_filter(sample_videos):
    report = ClickbaitReport()
    filtered_videos = report.filter_videos(sample_videos)

    assert len(filtered_videos) == 4
    assert all(video.ctr > 15 for video in filtered_videos)
    assert all(video.retention_rate < 40 for video in filtered_videos)


def test_clickbait_sorting(sample_videos):
    report = ClickbaitReport()
    filtered_videos = report.filter_videos(sample_videos)

    ctrs = [video.ctr for video in filtered_videos]
    assert ctrs == sorted(ctrs, reverse=True)


def test_report_factory():
    report = ReportFactory.get_report("clickbait")

    assert report.name == "Clickbait"

    with pytest.raises(ValueError):
        ReportFactory.get_report("test_report")

