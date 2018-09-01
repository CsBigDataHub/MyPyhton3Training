#!/usr/bin/python3
# break.py 



def main():
    s = 'this is a string'
    for c in s:
        #if c=='s':continue
        if c=='s':break
        print(c, end='')

if __name__ == "__main__": main()
