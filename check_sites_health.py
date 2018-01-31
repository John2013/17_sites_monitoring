import argparse

import requests
from os.path import isfile
from datetime import datetime, timedelta
import whois


def read_urls_file(path):
    with open(path) as file:
        for url in file.read().split('\n'):
            yield url


def is_server_respond_is_ok(url):
    try:
        return requests.get(url).ok
    except requests.exceptions.ConnectionError:
        return False


def get_domain_expiration_date(url, days_count):
    expiration_date = whois.whois(url).expiration_date
    if type(expiration_date) is list:
        expiration_date = expiration_date[0]
    if expiration_date is None:
        return False
    return datetime.now() + timedelta(days=days_count) < expiration_date


def print_bool(boolean):
    return '✔' if boolean else '✘'


def get_args():
    parser = argparse.ArgumentParser(
        description='Отображает информацию о работоспособности сайтов'
    )
    parser.add_argument(
        '--urls',
        '-u',
        type=str,
        metavar='URLS_FILE',
        dest='urls_file',
        help='Путь к файлу со списком ссылок',
        required=True
    )
    parser.add_argument(
        '--days',
        '-d',
        type=int,
        metavar='DAYS_COUNT',
        dest='days_count',
        help='Количество дней для проверки срока домена (по умолчанию - 30)',
        default=30
    )
    args = parser.parse_args()

    if not isfile(args.urls_file):
        parser.error('Файл со ссылками не найден')

    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()

    for url in read_urls_file(args.urls_file):
        print('url: {}'.format(url))
        print('http status 200: {}'.format(
            print_bool(is_server_respond_is_ok(url))
        ))
        print('домен на {} дней оплачен: {}\n'.format(
            args.days_count,
            print_bool(get_domain_expiration_date(url, args.days_count))
        ))
