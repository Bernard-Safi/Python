class Monnaie :
    def __init__(self,valeur,devise):
        self.valeur=valeur
        self.devise=devise
    def ajouter(self,monnaie):
        Monnaie.validateDevise(self,monnaie)
        self.valeur+=monnaie.valeur
    def retrancher(self,monnaie):
        Monnaie.validateDevise(self,monnaie)
        self.valeur-=monnaie.valeur
    def validateDevise(d1,d2):
        if d1.devise!=d2.devise:
            raise TypeError("different types de monnaie")
    def __repr__(self):
        return f"{self.valeur} {self.devise}"
#test
m1=Monnaie(5,"euros")
print("m1= ",m1)
m2=Monnaie(7,"euros")
print("m2= ",m2)
m1.ajouter(m2)
print("m1+m2= ",m1)
m1=Monnaie(5,"euros")
m2=Monnaie(7,"euros")
print("m1= ",m1)
print("m2= ",m2)
m1.retrancher(m2)
print("m1-m2= ",m1)
m1=Monnaie(5,"euros")
print("m1= ",m1)
m2=Monnaie(7,"dollar")
print("m2= ",m2)
m1.ajouter(m2)
print("m1+m2= ",m1)

