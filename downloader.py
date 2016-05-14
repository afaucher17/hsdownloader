#!/usr/bin/python3

import sys
import os

from html.parser import HTMLParser
import urllib.request, urllib.parse, urllib
from urllib.error import HTTPError, URLError

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag :", tag)
    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)
    def handle_data(self, data):
        print("Encountered some data :",  data)

def main(argv):
    try:
        req = urllib.request.Request('http://horriblesubs.info/lib/search.php?value=test', headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req).read()
    except HTTPError as e:
        print("Server return " + str(e.code) + " error")
        error = e
    except URLError as e:
        print("Can't reach server: " + e.reason)
        error = e
    else:
        parser = MyHTMLParser()
        parser.feed(res.decode("utf-8"))

if __name__ == "__main__":
    main(sys.argv)
