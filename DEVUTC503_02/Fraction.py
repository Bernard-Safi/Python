class Fraction:
    def __init__(self,num,denom):
        self.num=num
        self.denom=denom
    def __mul__(self,other):
        return Fraction.simplifier(self.num*other.num, self.denom*other.denom)
    def __add__(self,other):
        if self.denom==other.denom:
            self.num+=other.num
        else:
                self.num*=other.denom
                other.num*=self.denom
                self.denom*=other.denom
                self.num+=other.num
        return Fraction.simplifier(self.num, self.denom)
    def simplifier(a, b):
        facteur_commun = pgcd(a, b)
        a /= facteur_commun
        b /= facteur_commun
        return int(a), int(b)
def pgcd(a,b) :  
    while a%b != 0 : 
        a, b = b, a%b 
    return b
f1=Fraction(2,10)
f2=Fraction(3,8)
print(f1*f2)
f1=Fraction(4,2)
f2=Fraction(6,2)
print(f1+f2)
f1=Fraction(4,5)
f2=Fraction(6,15)
print(f1+f2)
f1=Fraction(3,4)
f2=Fraction(5,20)
print(f1*f2)