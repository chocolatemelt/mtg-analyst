#!/usr/bin/env python3
"""Generates sets.txt.

sets.txt is a file listing all set codes to be fetched via scryfall's /card
API. Any sets to be ignored should be included in the ignore list.
"""
import requests

if __name__ == '__main__':
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

