#!/usr/bin/python3
# functions.py 



def main():
    testfunc1(412,24)

def testfunc(number):
    print('This is a test function', number)

def testfunc1(number,another=None,onemore=75):
    print('This is a test function', number,another,onemore)

""" 
# pass wil pass the empty block of code
def testfunc():
    pass    
 """
if __name__ == "__main__": main()
