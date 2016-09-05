#!/usr/bin/env python

import sys, os
import requests
import json

def main(argv):
    query = argv[1]
    data = {
        "access_token": os.environ.get('GENIUS_TOKEN'),
        "q": query
    }
    request = requests.get('https://api.genius.com/search', params=data)
    result = request.json()
    hits = result['response']['hits']

    alfred_items = []

    for hit in hits:
        if hit['type'] != 'song':
            print('got unexpected hit type: {}'.format(hit['type']), 
                file=sys.stderr)
            continue

        hit_result = hit['result']

        alfred_items.append({
            "title": hit_result['title'],
            "subtitle": hit_result['primary_artist']['name'],
            "arg": hit_result['url'],
            "quicklookurl": hit_result['url']
        })

    print(json.dumps({
        "items": alfred_items
    }))
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
