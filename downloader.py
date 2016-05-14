#!/usr/bin/python3

import sys
import os

import urllib.request, urllib.parse, urllib
from urllib.error import HTTPError, URLError

def main(argv):
    req = urllib.request.Request('//http://horriblesubs.info/lib/search.php?value=test')

if __name__ == "__main__":
    main(sys.argv)
