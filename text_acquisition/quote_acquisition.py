from tqdm import tqdm
from text_acquisition.preloading import update_preload
from utils.constants import URL, TOPICS, TOPIC_CLASS, QUOTE_CLASS, PAGE_LINK_CLASS
from utils.html_parser import get_parsed_html, get_random_idx, find_classes


def chose_topic():
    links = find_classes(TOPICS, 'a', TOPIC_CLASS, href=True)

    assert len(links) > 0

    idx = get_random_idx(len(links)-1)
    href = links[idx]['href']
    
    return href


def get_quotes(url):
    quotes_html = get_parsed_html(url)
    divs = quotes_html.find_all('div', {'class': QUOTE_CLASS})
    divs = find_classes(url, 'div', QUOTE_CLASS)

    return divs 


def get_quote_links(topic_url): 
    quotes_html = get_parsed_html(topic_url)
    divs = quotes_html.find_all('div', {'class': QUOTE_CLASS})
    page_links = quotes_html.find_all('a', {'class': PAGE_LINK_CLASS}, href=True)

    return divs, page_links


def acquire_quotes(href):
    topic_url = URL + href
    divs, page_links = get_quote_links(topic_url)

    if page_links:
        max_page_number = int(page_links[-2].text)
        num = get_random_idx(max_page_number+1, 1)
        if num > 1:
            url = topic_url + f'_{num}'
            divs = get_quotes(url)

    return divs


def chose_quote(href, seen):
    divs = acquire_quotes(href)

    content = None
    while content in seen:
        idx = get_random_idx(len(divs)-1)
        quote = divs[idx].text
        quote, author = cleanup_quote(quote)
        content = quote + author

    return quote, author, content


def cleanup_quote(quote):
    quote = quote.strip()
    splits = quote.split('\n')
    return splits[0], splits[-1]


def get_quote(seen):
    topic = chose_topic()
    return chose_quote(topic, seen)