import requests
import sys
from os.path import isfile
from urllib.parse import urlparse
from datetime import datetime, timedelta
import whois


def load_urls4check(path):
    with open(path) as file:
        for url in file.read().split('\n'):
            yield url


def is_server_respond_with_200(url):
    try:
        return requests.get(url).ok
    except requests.exceptions.ConnectionError:
        return False


def get_domain_expiration_date(url, days_count):
    domain = urlparse(url).netloc
    expiration_date = whois.whois(domain).expiration_date
    if type(expiration_date) is list:
        expiration_date = expiration_date[0]
    if expiration_date is None:
        return False
    time = timedelta(days=days_count)
    return datetime.now() + time < expiration_date


def print_bool(boolean):
    return '✔' if boolean else '✘'


if __name__ == '__main__':
    if len(sys.argv) > 1 and isfile(sys.argv[1]):
        urls_path = sys.argv[1]
    else:
        exit("Файл со ссылками на проверяемые сайты не найден")

    if len(sys.argv) > 2 and int(sys.argv[2]) > 0:
        days_count = int(sys.argv[2])
    else:
        days_count = 30

    for url in load_urls4check(urls_path):
        print('url: {}'.format(url))
        print('http status 200: {}'.format(
            print_bool(is_server_respond_with_200(url))
        ))
        print('домен на {} дней оплачен: {}\n'.format(
            days_count,
            print_bool(get_domain_expiration_date(url, days_count))
        ))
