from dataclasses import dataclass


@dataclass
class VideoData:
    title: str
    ctr: float
    retention_rate: int
    views: int
    likes: int
    avg_watch_time: float

    @classmethod
    def from_csv_row(cls, row) -> "VideoData":
        return cls(
            title=row["title"],
            ctr=float(row["ctr"]),
            retention_rate=int(row["retention_rate"]),
            views=int(row["views"]),
            likes=int(row["likes"]),
            avg_watch_time=float(row["avg_watch_time"]),
        )
