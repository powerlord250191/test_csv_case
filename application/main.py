from tabulate import tabulate
from argparse import Namespace, ArgumentParser

from application.reader_csv import CSVReader
from application.report_function import ReportFactory


def parse_arguments() -> Namespace:
    parser = ArgumentParser(
        description="Утилита по поиску видео с ctr > 15% и процентом удержания < 40",
    )

    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Пути к CSV файлам с данными для анализа, допустимо указать несколько путей",
    )

    parser.add_argument(
        "--report",
        type=str,
        required=True,
        choices=["clickbait"],
        help="Тип ожидаемого отчёта",
    )

    return parser.parse_args()

def main():

    args = parse_arguments()

    total_videos = []
    reader = CSVReader()

    for path in args.files:
        try:
            videos = reader.read_file(path)
            total_videos.append(videos)
        except FileNotFoundError as ex:
            print(f"Ошибка при попытке прочитать файл {ex}")

    if not total_videos:
        print("Данных для анализа не найдено")

    report = ReportFactory.get_report(args.report)
    filtered_videos = report.filter_videos(total_videos)

    if filtered_videos:
        data = [report.format_row(video=video) for video in filtered_videos]
        headers = report.get_headers()
        print(tabulate(data, headers=headers, tablefmt="grid"))
    else:
        print("Видео соответствующих критериям отчёта не найдено")


if __name__ == '__main__':
    main()