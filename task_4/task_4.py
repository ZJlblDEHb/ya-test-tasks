# -*- coding: utf-8 -*-


__author__ = 'asergeev'


import os
from collections import Counter


LOG_FILE = "access.log"


def get_ip(row):
    row_list = row.split(' ')
    if len(row_list) > 0:
        return row_list[0]
    else:
        raise ValueError('Found broken row in file!')


def main():
    counter = Counter()
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), LOG_FILE), 'r') as f:
        for row in f:
            counter.update((get_ip(row), ))

    for ip, count in counter.most_common(10):
        print "%d - %s" % (count, ip)


if __name__ == '__main__':
    main()