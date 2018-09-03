#!/usr/bin/python3
# strings.py 



def main():
    s = 'this is a string'
    print(s.capitalize())
    print(s.title())
    print(s.upper())
    print(s.swapcase())
    print(s.find('is'))
    print(s.replace('this', 'that'))
    print(s.strip())
    print(s.isalnum())
    print(s.isalpha())
    print(s.isdigit())
    print(s.isprintable())

    #format replace
    d= dict(bob='a',fred='b')
    s= 'This is {bob} and that is {fred}'.format(**d)
    print(s)

    split_s = s.split()
    for w in split_s : print(w)

    new_s = ";".join(split_s)  

    print(new_s)  

if __name__ == "__main__": main()
