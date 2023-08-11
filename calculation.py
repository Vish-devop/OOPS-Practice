
# class AbstractBaseClass:

#     def add(self):
#         pass
    
#     def subtract(self):
#         pass

#     def multiply(self):
#         pass

#     def divide(self):
#         pass

class Calcultion():

    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    
    add = lambda self: self.num1+self.num2
    subtract=lambda self: self.num1-self.num2
    multiply=lambda self: self.num1*self.num2
    divide = lambda self: (self.num1 // self.num2) if (self.num2 != 0) else (f"{self.num1} can-not be divided by 0")

    
    
