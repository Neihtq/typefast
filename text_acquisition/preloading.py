import os
import csv

from utils.constants import CACHE_PATH


def preload_exists():
    return os.path.exists(CACHE_PATH)


def preload():
    with open(CACHE_PATH) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        data = [row for row in csv_reader]

    return data if data[-1] else data[-1]


def update_preload(data):
    with open(CACHE_PATH, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in data:
            csv_writer.writerow(row)
