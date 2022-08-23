import sys
import time
import curses

from tqdm import tqdm
from text_acquisition.quote_acquisition import chose_topic, chose_quote, cleanup_quote, get_quotes, crawl_all_quotes
from utils.utils import measure_time
from utils.cli_utils import update_console
from utils.html_parser import get_parsed_html, get_random_idx
from utils.constants import TOPICS, TOPIC_CLASS, URL, QUOTE_CLASS, PAGE_LINK_CLASS


def get_topics_less_2_pages():
    topics_html = get_parsed_html(TOPICS)
    links = topics_html.find_all('a', {'class': TOPIC_CLASS}, href=True)
    hrefs = [link['href'] for link in links]

    exceptions = []
    for href in tqdm(hrefs):
        topic_url = URL + href
        quotes_html = get_parsed_html(topic_url)
        divs = quotes_html.find_all('div', {'class': QUOTE_CLASS})
        page_links = quotes_html.find_all('a', {'class': PAGE_LINK_CLASS}, href=True)

        try:
            max_page_number = int(page_links[-2].text)
        except: 
            print(page_links)
            exceptions.append(href)

    for e in exceptions:
        print(e)


def throw_exception():
    console = curses.initscr()
    console.clear()
    console.addstr(0, 0, 'test')
    console.refresh()

    time.sleep(1)

    try:
        x = 1 / 0
    except Exception as e:
        curses.endwin() 
        time.sleep(1)
        print('Ended window')
        time.sleep(1)
        raise e


def catch_keypress():
    console = curses.initscr() 
    update_console(0, 0, "Press any key", console)

    while True:
        key = console.getch()
        update_console(1, 0, str(key), console)
        if key == 3:
            update_console(2, 0, 'KeyboardInterrupt', console)
            sys.exit()


def quote_acquisition_time():
    duration, topic = measure_time(chose_topic)
    print(f'Chose topic: {duration}s')

    duration, quote = measure_time(chose_quote_timed, (topic, {None}))
    print(f'Chose quote: {duration}s')

    duration, (clean_quote, author) = measure_time(cleanup_quote, (quote,))
    print(f'Cleanup quote: {duration}s')


def chose_quote_timed(href, seen):
    start = time.time()
    topic_url = URL + href
    quotes_html = get_parsed_html(topic_url)
    end = time.time()
    print(f'HTML parse: {end-start}s')

    start = time.time()
    divs = quotes_html.find_all('div', {'class': QUOTE_CLASS})
    end = time.time()
    print(f'Find div: {end-start}s')

    start = time.time()
    page_links = quotes_html.find_all('a', {'class': PAGE_LINK_CLASS}, href=True)
    end = time.time()
    print(f'Find a: {end-start}s')
    
    start = time.time()
    if page_links:
        max_page_number = int(page_links[-2].text)
        for num in range(2, max_page_number + 1):
            url = topic_url + f'_{num}'
            get_quotes(url, divs)
    end = time.time()
    print(f'navigate pages: {end-start}s')

    start = time.time()
    quote_div = None
    while quote_div in seen:
        idx = get_random_idx(len(divs)-1)
        quote_div = divs[idx]

    seen.add(quote_div)
    end = time.time()
    print(f'update set: {end-start}s')

    return quote_div.text


if __name__ == '__main__':
    #get_topics_less_2_pages()
    #throw_exception()
    #catch_keypress()
    #quote_acquisition_time() 
    crawl_all_quotes()