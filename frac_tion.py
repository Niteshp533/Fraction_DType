class Fraction:
     
    def __init__(self,n, d = 1):  # we use constructor to impl. configuration related task, which is not executed manually. eg: DB connection, GPS connection etc.
        self.num = n         # within a class we cannot call one method to another method(s) of same class, so that we use "Self" as cuurent object.
        self.den= d
            
    def __str__(self):
        return f'{self.num}/{self.den}'
            
    def __add__(self,other):
        temp_num = self.num * other.den + self.den * other.num
        temp_den = self.den * other.den
        return f'{temp_num}/{temp_den}' 
            
    def __sub__(self,other):
        temp_num = self.num * other.den - self.den * other.num
        temp_den = self.den * other.den
        return f'{temp_num}/{temp_den}'
            
    def __mul__(self,other):
        temp_num = self.num * other.num
        temp_den = self.den * other.den
        return f'{temp_num}/{temp_den}' 

    def __truediv__(self,other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num
        return f'{temp_num}/{temp_den}' 
    
    def gcd(self, others):
        def Gcd(a,b):
            if b == 0:
                return a
            else:
                return Gcd(b,a%b)
        temp_num = Gcd(self.num, others.num)
        temp_den = (self.den * others.den) // Gcd(self.den, others.den)
        return f'{temp_num}/{temp_den}'

    def lcm(self, others):
        def Gcd(a,b):
            if b == 0:
                return a
            else:
                return Gcd(b,a%b)
        temp_num = (self.num * others.num) // Gcd(self.num, others.num)
        temp_den = Gcd(self.den, others.den)
        return f'{temp_num}/{temp_den}'
                
frac_num1 = Fraction(12,34)
frac_num2 = Fraction(23)

print(frac_num1,frac_num2)  # output: 12/34 23/1