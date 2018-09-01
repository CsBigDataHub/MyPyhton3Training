#!/usr/bin/python3
# switch.py 



def main():
    print('this is the switch.py file')
    d3 = dict(
        one=1,two=2,three=3,four=4
    )
    v='seven'
    print(d3.get(v,"other value")) #This will give vale if `V` exists in the dictionary else give the value in the braces

if __name__ == "__main__": main()
