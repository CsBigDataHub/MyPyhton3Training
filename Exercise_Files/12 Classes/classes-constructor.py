#!/usr/bin/python3
# classes.py 



class Duck:
    def __init__(self, value):
            self._value=value
    def quack(self):
        print('Quaaack!', self._value)

    def walk(self):
        print('Walks like a duck.', self._value)

def main():
    donald = Duck(43)
    peter = Duck(100)
    donald.quack()
    donald.walk()
    peter.quack()
    peter.walk()

if __name__ == "__main__": main()
