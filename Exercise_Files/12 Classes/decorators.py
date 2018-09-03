#!/usr/bin/python3
# classes.py 



class Duck:
    def __init__(self, **kwargs):
        self.properties = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)

    @property
    def color(self):
        return self.properties.get('color',None)

    @color.setter
    def color(self, colr):
        self.properties['color']=colr

    @color.deleter
    def color(self):
        del self.properties['color']

def main():
    #donald = Duck(color = 'blue')
    donald = Duck()
    #setter
    donald.color='white'
    #getter
    print(donald.color)
    #deleter
    del(donald.color)
    print("After delete",donald.color)
    #print(donald.get_property('color'))

if __name__ == "__main__": main()
