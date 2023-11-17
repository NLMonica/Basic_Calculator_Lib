import math

class calculation:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def addition(self):
        a = self.a
        b = self.b
        print(dir(self))
        print("The ans is " +str(int(a) + int(b)))
    
    def substraction(self):
        a = self.a
        b = self.b
        print("The ans is " +str(int(a) * int(b)))

    def multiplication(self):
        a = self.a
        b = self.b
        print("The ans is " +str(int(a) * int(b)))
    
    def division(self):
        a = self.a
        b = self.b
        print("The ans is " +str(int(a) / int(b)))

    def sqrt(self):
        a = self.a
        b = self.b
        print("The ans is " +str(int(math.sqrt(a))))
        print("The ans is " +str(int(math.sqrt(b))))
        
    def sin(self):
        a = self.a
        b = self.b
        print("The ans is " +str(math.sin(a)))
        print("The ans is " +str(math.sin(b)))
        
    def cos(self):
        a = self.a
        b = self.b
        print("The ans is " +str(math.cos(a)))
        print("The ans is " +str(math.cos(b)))

    def tan(self):
        a = self.a
        b = self.b
        print("The ans is " +str(math.tan(a)))
        print("The ans is " +str(math.tan(b)))

        








