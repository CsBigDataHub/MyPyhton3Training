#!/usr/bin/python3
# for.py 



def main():
    fh = open('Exercise_Files/02 Quick Start/lines.txt')
    for line in fh.readlines():
        print(line,end='')
    for index, line in enumerate(fh.readlines()):
        print(index,line,end='')   
    s = 'this is a string'
    for i,c in enumerate(s):
        print(i,c)
        if c == 's':print('index {} is an s'.format(i))

if __name__ == "__main__": main()
