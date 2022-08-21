import random
import requests
from bs4 import BeautifulSoup as bs


def get_html(url):
    return requests.get(url).text


def parse_html(html):
    return bs(html, 'html.parser')


def get_parsed_html(url):
    html_doc = get_html(url)
    return parse_html(html_doc)


def get_random_idx(end, start=0):
    return random.randint(start, end)