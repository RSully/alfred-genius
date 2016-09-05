#!/usr/bin/env python

import sys, os
import requests
import json
from urllib.parse import urlparse

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

        # At the moment Genius is not returning secure URLs
        # Also, at the moment these HTTPS urls all redirect back to HTTP
        # so this is kind of useless. But hopefully that changes.
        hit_url = urlparse(hit_result['url'])._replace(scheme='https').geturl()

        alfred_items.append({
            "uid": 'https://api.genius.com{}'.format(hit_result['api_path']),
            "title": hit_result['title'],
            "subtitle": hit_result['primary_artist']['name'],
            "arg": hit_url,
            "quicklookurl": hit_url
        })

    print(json.dumps({
        "items": alfred_items
    }))
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
