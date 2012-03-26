#!/usr/bin/python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : rssPy.py
# Creation Date : 26-03-2012
# Last Modified : Mon 26 Mar 2012 11:16:18 AM EEST
# Created By : Greg Liras <gregliras@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/
from sys import argv
from urllib2 import Request, urlopen
from re import compile,findall,sub

def main():
    if not len(argv) >= 2:
        print "Usage: %s <url> <titles>"%argv[0]
    req = Request(argv[1])
    response = urlopen(req)
    the_page = response.read()
    regexp = compile(r'<title.*?\/title>')
    titles = findall(regexp,the_page)
    regexp = compile(r'</?title[^>]*>')
    titles = map(lambda s:sub(regexp, '',s),titles)
    for i in range(int(argv[2])):
        print titles[i]
    



if __name__=="__main__":
    main()

