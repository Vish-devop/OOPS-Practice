
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

    def add(self):
        return self.num1+self.num2
    
    def subtract(self):
        return self.num1-self.num2

    def multiply(self):
        return self.num1*self.num2

    def divide(self):
        if self.num2==0:
            print(f"{self.num1} can-not be divided by 0")
        return self.num1//self.num2
    
