import os
import csv

from utils.constants import PRELOAD_TEXT

CURR_PATH = os.path.dirname(os.path.abspath(__file__))
PRELOAD_PATH = os.path.join('..', '..', 'data', CURR_PATH, PRELOAD_TEXT)


def preload_exists():
    return os.path.exists(PRELOAD_PATH)


def preload():
    with open(PRELOAD_PATH) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        data = [row for row in csv_reader]

    return data


def update_preload(data):
    print(PRELOAD_PATH)
    with open(PRELOAD_PATH, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in data:
            csv_writer.writerow(row)
