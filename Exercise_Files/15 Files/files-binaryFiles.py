#!/usr/bin/python3
# files.py 

def main():
    buffersize = 50000
    inFile = open('Exercise_Files/15 Files/olives.jpg', mode='rb')
    outFile = open('Exercise_Files/15 Files/olives-new-duplicate.jpg', mode='wb')
    buffer = inFile.read(buffersize)
    while len(buffer):
        outFile.write(buffer)
        print('.',end='')
        buffer = inFile.read(buffersize)
    print()
    print('Done.')
if __name__ == "__main__": main()
