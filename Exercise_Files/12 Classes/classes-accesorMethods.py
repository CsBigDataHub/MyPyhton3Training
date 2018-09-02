#!/usr/bin/python3
# classes.py 



class Duck:
    def __init__(self, color='green'):
            self._color=color

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    @property
    def get_color(self):
        return self._color
    
    @get_color.setter
    def set_color(self,color):
        self._color=color
            

def main():
    donald = Duck()
    print(donald.get_color)
    donald.set_color = 'red'
    print(donald.get_color)
    """ peter = Duck()
    donald.quack()
    donald.walk()
    peter.quack()
    peter.walk() """

if __name__ == "__main__": main()
