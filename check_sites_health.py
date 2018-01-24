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


def get_domain_expiration_date(url):
    domain = urlparse(url).netloc
    expiration_date = whois.whois(domain).expiration_date
    if expiration_date is None:
        return False
    one_month = timedelta(hours=24 * 30)
    return datetime.now() + one_month < expiration_date


def print_bool(boolean):
    if boolean:
        return '✔'
    return '✘'


if __name__ == '__main__':
    if len(sys.argv) > 1 and isfile(sys.argv[1]):
        urls_path = sys.argv[1]
    else:
        exit("Файл со ссылками на проверяемые сайты не найден")

    for url in load_urls4check(urls_path):
        print('url: {}'.format(url))
        print('http status 200: {}'.format(
            print_bool(is_server_respond_with_200(url))
        ))
        print('Следующий месяц оплачен: {}\n'.format(
            print_bool(get_domain_expiration_date(url))
        ))
