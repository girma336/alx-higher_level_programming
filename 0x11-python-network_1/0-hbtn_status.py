#!/usr/bin/python3

import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        data = res.read()
        print("Body responses:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode('utf8')))
