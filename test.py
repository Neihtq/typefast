import sys
import curses

from tqdm import tqdm
from utils.cli_utils import update_console
from utils.html_parser import get_parsed_html
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


def catch_keypress():
    console = curses.initscr() 
    update_console(0, 0, "Press any key", console)

    while True:
        key = console.getch()
        update_console(1, 0, str(key), console)
        if key == 3:
            update_console(2, 0, 'KeyboardInterrupt', console)
            sys.exit()




if __name__ == '__main__':
    #get_topics_less_2_pages()
    catch_keypress()