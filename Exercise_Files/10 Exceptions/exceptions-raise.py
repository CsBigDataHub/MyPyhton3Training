#!/usr/bin/python3
# exceptions.py 

# python exception link : https://docs.python.org/3.7/library/exceptions.html

def main():
    try:
        for line in readFile('/home/linuxlite/Downloads/Python3 essential Exercise Files/Ex_Files_Python_3_EssT/Exercise_Files/10 Exceptions/xlines.doc'): print(line.strip())        
    except IOError as e:
        print('could not find the file :',e,'please check the path or file name')
    except ValueError as e:
        print('bad file name',e)    

def readFile(fileName):
    if fileName.endswith('.txt'):
        fh = open(fileName)
        return fh.readlines()
    else:
        raise ValueError('file name must end with .txt ')    

if __name__ == "__main__": main()
