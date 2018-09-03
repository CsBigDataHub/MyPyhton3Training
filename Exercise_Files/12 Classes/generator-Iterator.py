#!/usr/bin/python3
# classes.py 

class inclusive_range:
    def __init__(self, *args):
        numargs=len(args)
        if numargs<1: raise TypeError('requires at least one argument')
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start,self.stop) = args
            self.step =1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else: raise TypeError('inclusive_range excepted at most 3 arguments, got{}'.format(numargs))

    def __iter__(self):
        i= self.start
        while i <= self.stop:
            yield i
            i+=self.step 

def main():
    #o = inclusive_range(10)
    #for i in o: print(i, end = ' ')
    for i in inclusive_range(10) : print(i, end = ' ')

if __name__ == "__main__": main()
