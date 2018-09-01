#!/usr/bin/python3

# read the lines from the file
fh = open('Exercise_Files/02 Quick Start/lines.txt')
for line in fh.readlines():
    print(line,end='')
