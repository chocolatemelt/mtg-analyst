#!/usr/bin/env python3
import requests

r = requests.get("https://api.scryfall.com/sets").json()
r = r['data']
ignore = [
        '4bb',
        'fbb',
        'sum'
        ]
for s in r:
    if s['set_type'] == 'commander' or s['set_type'] == 'core' or s['set_type'] == 'expansion':
        if s['code'] not in ignore:
            print(s['code'])

