from tqdm import tqdm
from text_acquisition.preloading import update_preload
from utils.constants import URL, TOPICS, TOPIC_CLASS, QUOTE_CLASS, PAGE_LINK_CLASS
from utils.html_parser import get_parsed_html, get_random_idx, find_classes


def chose_topic():
    links = find_classes(TOPICS, 'a', TOPIC_CLASS, href=True)
    idx = get_random_idx(len(links)-1)
    href = links[idx]['href']
    
    return href


def get_quotes(url, all_divs):
    quotes_html = get_parsed_html(url)
    divs = quotes_html.find_all('div', {'class': QUOTE_CLASS})
    divs = find_classes(url, 'div', QUOTE_CLASS)
    all_divs += divs


def get_quote_links(topic_url): 
    quotes_html = get_parsed_html(topic_url)
    divs = quotes_html.find_all('div', {'class': QUOTE_CLASS})
    page_links = quotes_html.find_all('a', {'class': PAGE_LINK_CLASS}, href=True)

    return divs, page_links


def navigate_all_pages(page_links, divs, topic_url):
    max_page_number = int(page_links[-2].text)
    for num in range(2, max_page_number + 1):
        url = topic_url + f'_{num}'
        get_quotes(url, divs)


def acquire_quotes(href):
    topic_url = URL + href
    divs, page_links = get_quote_links(topic_url)

    if page_links:
        navigate_all_pages(page_links, divs, topic_url)

    return divs


def chose_quote(href, seen):
    divs = acquire_quotes(href)

    quote_div = None
    while quote_div in seen:
        idx = get_random_idx(len(divs)-1)
        quote_div = divs[idx]

    seen.add(quote_div)

    return quote_div.text


def cleanup_quote(quote):
    quote = quote.strip()
    splits = quote.split('\n')
    return splits[0], splits[-1]


def get_quote(seen):
    topic = chose_topic()
    quote = chose_quote(topic, seen)
    clean_quote, author = cleanup_quote(quote)

    return clean_quote, author


def crawl_all_quotes():
    links = find_classes(TOPICS, 'a', TOPIC_CLASS, href=True)
    data = []
    for link in tqdm(links):
        href = link['href']
        divs = acquire_quotes(href)

        for div in tqdm(divs):
            quote, author = cleanup_quote(div.text)
            data.append([quote, author])

    print('Write csv.')
    update_preload(data)
