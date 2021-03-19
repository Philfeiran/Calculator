import  math

def addition(a,b):
    return a+b
def subtraction(a,b):
    return b-a
def multiplication(a,b):
    return  a*b
def Division(a,b):
    return b/a
def Square(a):
    return  a*a
def SquareRoot(a):
    return math.sqrt(a)

class calculator:
    result = 0
    def __init__(self):
        self.result =0
        pass

    def add(self,x,y):
        result =addition(x,y)
        return result
    def minus(self,x,y):
        result = subtraction(x,y)
        return result
    def multply(self,x,y):
        result = multiplication(x,y)
        return result
    def divide(self,x,y):
        result = Division(x,y)
        return result

    def square(self,x):
        result = Square(x)
        return result
    def squareRoot(self,x):
        result= SquareRoot(x)
        return result
