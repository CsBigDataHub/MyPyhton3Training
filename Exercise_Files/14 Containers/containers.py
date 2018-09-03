#!/usr/bin/python3
# containers.py 



def main():
    print('This is the containers.py file. to convert byte code')
    fileIn = open('Exercise_Files/14 Containers/utf8.txt', mode='r', encoding='utf-8')
    fileOut = open('Exercise_Files/14 Containers/utf8-decoded.html', mode ='w')
    outbytes = bytearray()
    for line in fileIn:
        for word in line:
            if ord(word) > 127:
                outbytes += bytes('&#{:04d};'.format(ord(word)), encoding='utf-8')
            else: outbytes.append(ord(word))
    
    outStr = str(outbytes, encoding='utf-8')

    print(outStr,file=fileOut)
if __name__ == "__main__": main()
