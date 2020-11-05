n=-1;
while n<=1:
    n=int(input("Donner un nombre positif superieur a 1 : "));

def diviseur(n):
    
    i=2
    while i<n:
        if n%i == 0:
            break
        i=i+1
    return i
print(diviseur(n))