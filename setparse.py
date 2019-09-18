#!/usr/bin/env python3
import json
import requests
import sys
from datetime import datetime

def setparse(mtgset, output):
    sys.stdout = output
    more = True
    setdata=[]
    api = "https://api.scryfall.com/cards/search?q=set=" + mtgset
    while(more):
        scrydata = requests.get(api).json()
        more = scrydata['has_more']
        if more:
            api = scrydata['next_page']
        setdata.extend(scrydata['data'])
    ima = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def process(card):
        card.update({"timestamp":ima})
        return card

    carddata = list(map(process, setdata))

    count = 0
    for card in carddata:
        if sys.stdout is not sys.__stdout__:
            count += 1
            sys.__stdout__.write('>')
        print(json.dumps(card))

    if sys.stdout is not sys.__stdout__:
        sys.__stdout__.write('\nprocessed ' + str(count) + ' cards from ' + mtgset + '\n')

if __name__ == '__main__':
    setparse(sys.argv[1], sys.__stdout__)
