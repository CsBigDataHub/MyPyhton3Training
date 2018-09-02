#!/usr/bin/python3
# regex.py 

# 

import re

def main():
    fh = open('/home/linuxlite/Downloads/Python3 essential Exercise Files/Ex_Files_Python_3_EssT/Exercise_Files/09 Regexes/raven.txt')
    pattern = re.compile('(Len|Neverm)ore',re.IGNORECASE)
    for line in fh:
        if re.search(pattern,line):
            print(pattern.sub('###',line),end='')
       

if __name__ == "__main__": main()
