#!/usr/bin/python3
# functions.py 



def main():
    testfunc(412,24,2,3,4,45,5,6,76,87)

def testfunc(this, that,other,*args):
    #print(this,that,other,args)
    print(this,that,other)
    for n in args: print(n,end=' ')

if __name__ == "__main__": main()
