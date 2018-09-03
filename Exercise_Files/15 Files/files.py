#!/usr/bin/python3
# files.py 



def main():
    f = open('Exercise_Files/15 Files/lines.txt')
    for line in f.readlines():
        print(line, end = '')

if __name__ == "__main__": main()
