#!/usr/bin/python3
"""
   by using system Python script that takes in a URL,
   sends a request to the URL and displays the
   value of the
"""
import sys
import urllib.request

if __name__ == '__main__':

    with urllib.request.urlopen(sys.argv[1]) as res:
        print("{}".format(res.info().get('x-request-id')))
