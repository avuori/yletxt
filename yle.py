#!/usr/bin/python
# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import re
import urllib2

def fetch_data():
    return urllib2.urlopen("http://www.yle.fi/tekstitv/txt/P100_01.html").read()

def print_http_headers(content_length):
    print "\n".join((
                     "Expires: -1",
                     "Cache-Control: private, max-age=0",
                     "Content-Type: text/html; charset=UTF-8",
                     "Content-Length: %d" % content_length,
                   ))
    print "\n"

response_text = "";
soup = BeautifulSoup(fetch_data())
bigs = soup.findAll('big')
for big in bigs:
    m = re.search('<big><a href="([^"]+)">(\d+)</a>(.+)</big>', str(big))
    if m:
        href = m.group(1)
        page = m.group(2)
        title = m.group(3)
        response_text += '<div class="item"><a href="%s">%s</a> %s</div>\n' % (href, page, title)


print_http_headers(len(response_text))
print response_text
