#!/usr/bin/python3
# syntax.py 



class Egg:
    def __init__(self, kind= "fried"):
           self.kind = kind

    def whatKind(self):
        return self.kind        

def main():
    fried = Egg()
    scambled = Egg('scambled')
    print(scambled.whatKind())
    print(fried.whatKind())
    print("This is the syntax.py file.")

if __name__ == "__main__": main()
