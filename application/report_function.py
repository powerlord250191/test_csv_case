from abc import ABC, abstractmethod

from application.models import VideoData


class Report(ABC):

    @abstractmethod
    def filter_videos(self, videos: list[VideoData]) -> list[VideoData]:
        pass

    @abstractmethod
    def get_headers(self) -> list[str]:
        pass

    @abstractmethod
    def format_row(self, video: VideoData) -> list[str | float | int]:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass


class ClickbaitReport(Report):

    def filter_videos(self, videos: list[VideoData]) -> list[VideoData]:
        new_videos = []
        for video_list in videos:
            for video in video_list:
                new_videos.append(video)

        filtered_videos = [
            video for video in new_videos
            if video.ctr > 15 and video.retention_rate < 40
        ]

        return sorted(filtered_videos, key=lambda v: v.ctr, reverse=True)

    def get_headers(self) -> list[str]:
        return ["title", "ctr", "retention_rate"]

    def format_row(self, video: VideoData) -> list[str | float | int]:
        return [
            video.title,
            video.ctr,
            video.retention_rate,
        ]

    @property
    def name(self) -> str:
        return "Clickbait"

class ReportFactory:

    _reports = {
        "clickbait": ClickbaitReport,
    }

    @classmethod
    def get_report(cls, report_name: str) -> Report:
        report_class = cls._reports.get(report_name.lower())

        if not report_class:
            available_reports = ", ".join(cls._reports.keys())
            raise ValueError(
                f"Название отчёта {report_name} не найдено.\n"
                f"Доступны следующие отчёты: {available_reports}"
            )
        return report_class()

    @classmethod
    def register_report(cls, name: str, report_class: type):
        cls._reports[name.lower()] = report_class