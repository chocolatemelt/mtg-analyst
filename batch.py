#!/usr/bin/env python3
import bz2
import requests
import setparse
import sys
import tarfile
import time
from datetime import datetime

import config

def batch_recv():
    """Batch downloads cards from sets given in the scryfall API.

    Retrieves all cards from the listed sets in sets.txt using the scryfall API,
    inserting the mandated 100ms delay between API calls to reduce server load
    on the scryfall side.

    sets.txt is formatted exclusively as a newline-delimited text file of set
    codes as noted under the key ['code'] from the scryfall set API.
    """
    output = datetime.now().strftime('%Y-%m-%d') + '-dump.json'
    outf = open('data/' + output, 'w+')
    outf.truncate(0)
    f = open('sets.txt', 'r')
    for mtgset in f.readlines():
        setparse.setparse(mtgset, outf)
        time.sleep(1)

def cfj(filename = None):
    """Emulates tar cfj for a given file under the data folder.

    Arguments:
        filename
            A named file under the data/ folder.
    """
    if not filename:
        filename = datetime.now().strftime('%Y-%m-%d') + '-dump.json'
    output = filename + '.tar.bz2'
    with tarfile.open(output, 'w:bz2') as tar:
        tar.add('data/' + filename, arcname = filename)

def xf(filename = None):
    """Emulates tar xf for a given tar.bz file.

    Arguments:
        filename
            A named file.
    """
    if not filename:
        filename = datetime.now().strftime('%Y-%m-%d') + '-dump.json.tar.bz2'
    tar = tarfile.open(filename, 'r:bz2')
    tar.extractall('data/')
    tar.close()

def up(filename):
    files = { 'file': open(filename, 'rb') }
    print(requests.post(config.api, files=files).text)

def dl(filename):
    r = requests.get(config.api + '?file=' + filename, allow_redirects=True)
    open(filename, 'wb').write(r.content)

if __name__ == '__main__':
    dl(sys.argv[1])
