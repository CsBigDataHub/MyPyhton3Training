#!/usr/bin/python3

class Animal:
    def talk(self): print('I have something to say')
    def walk(self): print('Hey! Im walking here')
    def clothes(self): print('I Have nice clothes')


class Duck(Animal):
    def quack(self):
        print('Quaaaack')

    def walk(self):
        super().walk()
        print('walks like a duck')

class Dog(Animal):
    def clothes(self):
        print("I do not need clothes. I have fur")
 

 
def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    donald.clothes()

    fido = Dog()
    fido.clothes()
    fido.walk()


 
if __name__ == "__main__": main()
