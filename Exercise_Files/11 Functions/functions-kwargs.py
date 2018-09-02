#!/usr/bin/python3
# functions.py 



def main():
    testfunc(1,2,3,4,one=1,two=2,three=3)

def testfunc(*args, **kwargs):
    #print(this,that,other,args)
    for k in kwargs: print(k,kwargs[k])
    for n in args: print(n)

if __name__ == "__main__": main()
