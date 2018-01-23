#!/usr/bin/python
from BeautifulSoup import BeautifulSoup as bs
import urlparse
from urllib2 import urlopen
from urllib import urlretrieve
import os
import sys


def main(url, out_folder="/home/john/Videos/new/"):
    soup = bs(urlopen(url))
    for image in soup.findAll("a"):
        parsed = url+image['href']
        filename = image['href']
        outpath = os.path.join(out_folder, filename)
        try:
            urlretrieve(parsed, outpath)
        except:
            print "skipping" + parsed


if __name__ == "__main__":
    main("http://snubnose.brontosaurus.org/burning%20a/", "/home/john/Videos/new")

