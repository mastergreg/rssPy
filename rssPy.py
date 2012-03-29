#!/usr/bin/python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : rssPy.py
# Creation Date : 26-03-2012
# Last Modified : Thu 29 Mar 2012 09:01:17 AM EEST
# Created By : Greg Liras <gregliras@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/
from sys import argv
from urllib2 import Request, urlopen
from re import compile,findall,sub

def main():
    if not len(argv) >= 2:
        print "Usage: %s <url> <titles>"%argv[0]
    req = Request(argv[1],headers={'User-agent':'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'})
    response = urlopen(req)
    the_page = response.read()
    regexp = compile(r'<title.*?\/title>')
    titles = findall(regexp,the_page)
    regexp = compile(r'</?title[^>]*>')
    titles = map(lambda s:sub(regexp, '',s),titles)
    for i in range(int(argv[2])):
        print titles[i]
    return 0
    



if __name__=="__main__":
    main()

