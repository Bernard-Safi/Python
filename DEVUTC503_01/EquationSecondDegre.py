import math


def calculerDelta(a,b,c):
   return b*b-4*a*c


def resoudreSecondDegre(a,b,c):
   delta = calculerDelta(a,b,c)
   if delta > 0:
      
      val = [(-b-math.sqrt(delta))/(2*a),(-b+math.sqrt(delta))/(2*a)]
   elif delta < 0:
      val = "pas de solution"
   else:
      val = [-b/(2*a)] 
   return val

print("saisir a,b et c pour calculer ax2+bx+c=0")
a=0
while a==0:
    a=int(input("Donner a "))
b=int(input("Donner b "))
c=int(input("Donner c "))

print(resoudreSecondDegre(a,b,c))
