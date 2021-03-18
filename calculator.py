import  math
class calculator:
    def __init__(self):
        self.result =0

    def add(self,x,y):
        result = x+y
        return result
    def minus(self,x,y):
        result =x-y
        return result
    def multply(self,x,y):
        result = x*y
        return result
    def divide(self,x,y):
        result = x/y
        return result

    def square(self,x):
        result = x*x
        return result
    def squareRoot(self,x):
        result=math.sqrt(x)
        return result
