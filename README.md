# Sites Monitoring Utility

Отображает информацию о сайтах, отвечают ли они и оплачен ли домен на месяц.

# Как установить

Python 3 должен быть заранее установлен.
Используйте pip (или pip3 if если есть конфикты с Python 2) чтобы
установить пакеты:

```bash
pip install -r requirements.txt # или pip3
```

Рекомендуется использовать
[virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/)
для изоляции пакетов.

# Как использовать

1. Подготовьте файл с ссылками сайтов, разделённые переносами строк,
например:
```
https://ya.ru
https://google.ru
http://wbest.org
```

2. Запустите скрипт:

```bash
usage: check_sites_health.py [-h] --urls URLS_FILE [--days DAYS_COUNT]

Отображает информацию о работоспособности сайтов

Обязательный аргумент:
  --urls URLS_FILE, -u URLS_FILE
                        Путь к файлу со списком ссылок

Необязательные аргументы:
  -h, --help            show this help message and exit
  --days DAYS_COUNT, -d DAYS_COUNT
                        Количество дней для проверки срока домена (по
                        умолчанию - 30)
```

Пример:

```bash
python check_sites_health.py -u urls.txt -d 60
url: https://ya.ru
http status 200: ✔
домен на 60 дней оплачен: ✔

url: https://google.ru
http status 200: ✔
домен на 60 дней оплачен: ✘

url: http://wbest.org
http status 200: ✔
домен на 60 дней оплачен: ✔
```

# Цели проекта

Код создан в целях обучения.
Тренировочныекурсы для web-разработчиков - [DEVMAN.org](https://devman.org)
