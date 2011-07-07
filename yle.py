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
                     "Content-Type: text/html; charset=utf-8",
                     "Content-Length: %d" % content_length,
                   ))
    print "\n"

response_text = '';
soup = BeautifulSoup(fetch_data().decode("iso-8859-1"))
bigs = soup.findAll('big')
for big in bigs:
    m = re.search('<big><a href="([^"]+)">(\d+)</a>(.+)</big>', str(big))
    if m:
        href = m.group(1)
        inner = m.group(3)
	title = ''.join(BeautifulSoup(inner).findAll(text=True))
        response_text += '<div class="item"><a target="_blank" href="%s">%s</a></div>\n' % (href, title)


print_http_headers(len(response_text))
print response_text.encode("utf-8").replace("\xec\xb1\x84", "&auml;")
