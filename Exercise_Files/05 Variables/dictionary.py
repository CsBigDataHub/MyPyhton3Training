#!/usr/bin/python3
# variables.py


def main():
    d = {'one':1 , 'two':2 ,'three':3,'four':4,'five':5}
    d['six']=6
    for k in d:
        print(k,d[k])

    for k in sorted(d.keys()):
        print(k,d[k])
   
    d2 = dict(
        one=1,two=2,three=3,four=4
    )
    d2['seven'] = 7
    for k in d2:
        print(k,d2[k])


if __name__ == "__main__": main()
