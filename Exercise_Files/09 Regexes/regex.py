#!/usr/bin/python3
# regex.py 

# 

import re

def main():
    fh = open('/home/linuxlite/Downloads/Python3 essential Exercise Files/Ex_Files_Python_3_EssT/Exercise_Files/09 Regexes/raven.txt')
    for line in fh:
        if  re.search('(Len|Neverm)ore', line):
            print(line, end='')
        match = re.search('(Len|Neverm)ore',line)
        if match:
            print(match.group())
if __name__ == "__main__": main()
