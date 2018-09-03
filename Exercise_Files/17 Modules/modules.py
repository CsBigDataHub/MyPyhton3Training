#!/usr/bin/python3
# modules.py 



import sys

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)

    import os
    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd())

    import random
    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)

    import datetime
    now = datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)
    
""" 
    import urllib.request
    page = urllib.request.urlopen('http://google.com')
    for line in page: print(str(line, encoding= 'utf_8'), end='')
 """


if __name__ == "__main__": main()
