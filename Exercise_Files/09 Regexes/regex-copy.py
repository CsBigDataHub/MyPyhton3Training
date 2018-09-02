#!/usr/bin/python3
# regex.py 

# 

import re

def main():
    fh = open('/home/linuxlite/Downloads/Python3 essential Exercise Files/Ex_Files_Python_3_EssT/Exercise_Files/09 Regexes/raven.txt')
    for line in fh:
       #print(re.sub('(Len|Neverm|neverm)ore','###',line), end='')
       match = re.search('(Len|Neverm|neverm)ore',line)
       if match:
           print(line.replace(match.group(),'###'),end='')
if __name__ == "__main__": main()
