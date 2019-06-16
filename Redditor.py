#!/usr/bin/env python
import urllib.request
from bs4 import BeautifulSoup

print("[ REDDITOR v1.0 ]")

for a in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_':
    for b in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_':
        for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_':
            url = ("https://reddit.com/u/%s%s%s" % (a,b,c))
            req = urllib.request.Request(
                url,
                data=None,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
                    }
                )
            try:
                query = urllib.request.urlopen(req)
                query = query.read().decode('utf-8')
                soup = BeautifulSoup(query, 'html.parser')
                if "is either deleted, banned, or doesn't exist." in soup.get_text():
                    print("%s%s%s: AVAILABLE" % (a,b,c))
                else:
                    print("%s%s%s: TAKEN" % (a,b,c))
            except urllib.request.HTTPError as e:
                if e.code == 404:
                    print("%s%s%s: AVAILABLE" % (a,b,c))
                else:
                    print("%s%s%s: ERROR" % (a,b,c))
