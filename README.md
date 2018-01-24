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
python3 check_sites_health.py <path_to_urls_file>  # или python3
```

# Цели проекта

Код создан в целях обучения.
Тренировочныекурсы для web-разработчиков - [DEVMAN.org](https://devman.org)
