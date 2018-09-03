#!/usr/bin/python3
# files.py 



def main():
    buffersize = 50000
    inFile = open('Exercise_Files/15 Files/bigfile.txt', mode='r')
    outFile = open('Exercise_Files/15 Files/new-bigfile.txt', mode='w')
    buffer = inFile.read(buffersize)
    while len(buffer):
        outFile.write(buffer)
        print('.',end='')
        buffer = inFile.read(buffersize)
    print()
    print('Done.')
if __name__ == "__main__": main()
