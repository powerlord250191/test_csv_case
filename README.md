# test_csv_case
CLI приложение для обработки csv-файлов с метриками видео на YouTube. Приложение читает файлы с данными о видео и формирует отчеты. Формируется один отчёт, в котором будут перечислены кликбейтные видео - те, у которых одновременно высокий CTR и низкое удержание.

Для запуска необходимо установить все зависимости из файла requirements.txt, затем настроить консоль под работу с командой запуска "youtube-metrics --files data/stats1.csv data/stats2.csv --report clickbait", файл с настройками - setup.py. Команда для установки всех необходимых настроек "pip install -e ."
После этого можно запускат ьприложение в терминале командой - youtube-metrics --files data/stats1.csv data/stats2.csv --report clickbait.
Пример запуска на скриншоте ниже
<img width="1414" height="788" alt="image" src="https://github.com/user-attachments/assets/3fd856f4-ce59-4cbd-a601-9a90991d2a60" />

Провент покрытия кода тестами при проверке через pytest cov:
<img width="2040" height="758" alt="image" src="https://github.com/user-attachments/assets/9d341ba3-b128-4805-b592-e7a5f02ee3b6" />

Перед отправкой на гит хаб код был отформатирован и проверен следующими линтерами:
<img width="1020" height="532" alt="image" src="https://github.com/user-attachments/assets/4e7585cf-10d6-42ce-bad8-a49399e446c6" />
