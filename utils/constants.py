import os

# Text acquisition
URL = 'https://www.brainyquote.com'
TOPICS = URL + '/topics'
TOPIC_CLASS = 'topicIndexChicklet bq_on_link_cl'
QUOTE_CLASS = 'grid-item qb clearfix bqQt'
PAGE_LINK_CLASS = 'page-link'

# Menu
WELCOME = 'Type fast. Do you wanna start?'
GOODBYE = ' Ok bye.'
PROMPT = 'y/n'
RETRY = 'Do you wann try again?'
INVALID = 'Invalid answer. Please press "y" for "yes" or "n" for no.'
FETCHING = 'Fetching text...'
RESTART = 'Restart in'

# Notification
FINISHED = 'Done. Calculating your words per minuts (wpm) now...'
RESULT = 'Your Score:'

# paths
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join('..')

if not os.path.exists('cache'):
    os.makedirs('cache')

CACHE_PATH = os.path.join('cache', 'cache.csv')