#!/usr/bin/python3

import sys
import os

import BeautifulSoup

from html.parser import HTMLParser
import urllib.request, urllib.parse, urllib
from urllib.error import HTTPError, URLError

def main(argv):
    try:
        req = urllib.request.Request('http://horriblesubs.info/lib/search.php?value=test', headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req)
        soup = BeautifulSoup(res)
        elem = soup.findAll('a', {'href': 'link here'})
    except HTTPError as e:
        print("Server return " + str(e.code) + " error")
        error = e
    except URLError as e:
        print("Can't reach server: " + e.reason)
        error = e
    else:
        print(elem[0].href)

if __name__ == "__main__":
    main(sys.argv)
