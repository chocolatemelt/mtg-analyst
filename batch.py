#!/usr/bin/env python3
import setparse
from datetime import datetime

if __name__ == '__main__':
    output = datetime.now().strftime('%Y-%m-%d') + '-dump.json'
    outf = open('data/' + output, 'w+')
    outf.truncate(0)
    f = open('sets.txt', 'r')
    for mtgset in f.readlines():
        setparse.setparse(mtgset, outf)
