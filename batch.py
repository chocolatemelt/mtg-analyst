#!/usr/bin/env python3
"""Batch downloads cards from sets given in the scryfall API.

Retrieves all cards from the listed sets in sets.txt using the scryfall API,
inserting the mandated 100ms delay between API calls to reduce server load
on the scryfall side.

sets.txt is formatted exclusively as a newline-delimited text file of set
codes as noted under the key ['code'] from the scryfall set API.
"""
import setparse
import time
from datetime import datetime

if __name__ == '__main__':
    output = datetime.now().strftime('%Y-%m-%d') + '-dump.json'
    outf = open('data/' + output, 'w+')
    outf.truncate(0)
    f = open('sets.txt', 'r')
    for mtgset in f.readlines():
        setparse.setparse(mtgset, outf)
        time.sleep(1)
