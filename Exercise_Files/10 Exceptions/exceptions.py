#!/usr/bin/python3
# exceptions.py 

# 

def main():
    try:
        fh = open('/home/linuxlite/Downloads/Python3 essential Exercise Files/Ex_Files_Python_3_EssT/Exercise_Files/10 Exceptions/xlines.txt')
        for line in fh: print(line.strip())
    except IOError as e:
        print('could not find the file :',e,'please check the path or file name')

if __name__ == "__main__": main()
