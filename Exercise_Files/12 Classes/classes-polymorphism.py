#!/usr/bin/python3

class Duck():
    def quack(self):
        print('Quaaaack')

    def walk(self):
        print('walks like a duck')

    def bark(self):
        print('Ducks dont bark')

    def fur(self):
        print('Duck has feathers')

class Dog():
    def bark(self):
        print("woof!")
    
    def fur(self):
        print('the dog has brown and white fur')

    def walk(self):
        print('walks like a dog')

    def quack(self):
        print('dog do not quack')

def inTheForest(mydog):
    mydog.bark()
    mydog.fur()

def inThePond(duck):
    duck.quack()
    duck.walk()
 

 
def main():
    donald = Duck()
    fido = Dog()

    inTheForest(donald)
    inThePond(fido)

    """ for o in (donald,fido):
        o.quack()
        o.walk()
        o.fur()
        o.bark() """
   
if __name__ == "__main__": main()
