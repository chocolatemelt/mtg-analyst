#!/usr/bin/env python3
import json
import requests
import sys
from datetime import datetime

setdata = requests.get("https://api.scryfall.com/cards/search?q=set=" + sys.argv[1]).json()['data']
ima = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def process(card):
    card.update({"timestamp":ima})
    return card

carddata = list(map(process, setdata))

print(carddata)
