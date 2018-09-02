#!/usr/bin/python3
# classes.py 



class Duck:
    def __init__(self, **kwargs):
            self.variables = kwargs

    def set_variable(self,k,v):
        self.variables[k]=v

    def get_vaiable(self,k):
        return self.variables.get(k,None)   

"""
    def get_color(self):
        return self._color
    
    
    def set_color(self,color):
        self._color=color 
"""
            

def main():
    donald = Duck(color='white')
    print(donald.get_vaiable('color'))
    donald.set_variable('color','green')
    print(donald.get_vaiable('color'))
    donald1 = Duck(feet=2)
    print(donald1.get_vaiable('feet'))

   

if __name__ == "__main__": main()
