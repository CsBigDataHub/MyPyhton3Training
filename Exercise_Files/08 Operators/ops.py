#!/usr/bin/python3
# ops.py 



def main():
    print("This is the ops.py file.")
    list=[]
    list[:]=range(10)
    print(list)
    print(list[3])
    print(list[3:9])
    print(list[3:9:2]) # slice `:` operator in list can have 3 args 1- start index of list,2 -end of list , 3 - step over index
    list[3:9:2] = (99,99,99) # replacing the slices with 99
    print(list)
if __name__ == "__main__": main()
