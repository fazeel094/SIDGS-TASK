import math  #importing math module to calculate sine and cosine values
class Calculator:  #Defining class to bind all the functions
    def __init__(self,a,b):  #Writing a constructor with a,b as parameters(assuming numbers)
        self.a=a   # Assining to self(object)
        self.b=b
    def sumnums(self):  # Defining  a function to calculate sum
        Sumres=self.a+self.b  # Calculating sum for values from constructor
        print ("sum of given numbers is:", Sumres)
    def subnums(self):
        Subres=self.a-self.b
        print ("subtraction of given numbers is:", Subres)
    def mulnums(self):
        Mulres=self.a*self.b
        print ("multiplication of given numbers is:", Mulres)
    def divnums(self):
        if self.b!=0:
            Divres=self.a/self.b
            print ("Division of given numbers is:", Divres)
        else:
            print("cannot divide with 0")
    def sineofangle(self):
        Sinevalue=math.sin(math.radians(self.a))
        print ("sine value of given angle is:", Sinevalue)
    def cosineofangle(self):
        Cosinevalue=math.cos(math.radians(self.a))
        print ("cosine value of given angle is:", Cosinevalue)
test1 = Calculator(20,10)  # creating an object of calculator class
test1.sumnums()  # calling sum function using test1 object
test1.subnums()
test1.mulnums()
test1.divnums()
test1.sineofangle()
test1.cosineofangle()

        
