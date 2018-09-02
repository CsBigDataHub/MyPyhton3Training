#!/usr/bin/python3
# classes.py 



class Duck:
    def __init__(self, color='green'):
            self._color=color


   
    def get_color(self):
        return self._color
    
    
    def set_color(self,color):
        self._color=color
            

def main():
    donald = Duck()
    print(donald.get_color())
    donald.set_color('red')
    print(donald.get_color())
   

if __name__ == "__main__": main()
