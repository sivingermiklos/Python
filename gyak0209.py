import random
from xmlrpc.client import boolean

# FELADAT: Kérjen be három egész típusú számot és tárolja el, majd írja ki, hogy
#          melyik a nagyobb, melyik a kisebb, melyik a "középső" szám!
#          Feltételezheti, hogy a három szám nem egyenlő!

a : int = int(input("Add meg az 1. számot: "))
b : int = int(input("Add meg az 2. számot: "))
c : int = int(input("Add meg az 3. számot: "))

legnagyobb = max(a,b,c)
legkisebb = min(a,b,c)

if (a != legkisebb and a != legnagyobb):
    kozepso = a
    print("A 3 szám közül a 'középső' a(z): ",kozepso,sep = '')
elif (b != legkisebb and b != legnagyobb):
    kozepso = b
    print("A 3 szám közül a 'középső' a(z): ",kozepso,sep = '')
elif (c != legkisebb and c != legnagyobb):
    kozepso = c
    print("A 3 szám közül a 'középső' a(z): ",kozepso,sep = '')
    
    
print("A 3 szám közül a legnagyobb a(z): ",legnagyobb, sep = '')
print("A 3 szám közül a legkisebb a(z): ",legkisebb, sep = '')

lista = [a,b,c]
lista.sort()
print("Legkisebb: ",lista[0],"\nKözépső: ",lista[1], "\nLegnagyobb: ",lista[2])

# FELADAT 2: Tölts fel egy listát 10 darab kétjegyű egész számmal!
#            Lista elemeit írja ki a képernyőre.
#            Készíts egy függvényt prime néven, ami eldönti egy számról, hogy prímszám-e.
#            (Egy szám akkor prímszám, ha 1-el és magával osztható, pontosan 2 osztója van.)
#            Döntsd el, hogy a listában van-e prímszám.

# Lista létrehozása
lista = []
for i in range(10):
    lista.append(random.randint(10,99))
    print(lista[i])

# Prímszámot eldöntő függvény (paramétere egy egész szám, visszatérési értéke logikai érték)
def prime(szam: int) -> boolean:
    osztok = 0
    for i in range(szam):
        if szam%(i+1) == 0:
            osztok = osztok + 1
    return osztok == 2


# Eldöntöm, hogy a listában van-e prímszám
# version 1
vanebenneprim = False
for i in range(10):
    if(prime(lista[i])):
        vanebenneprim = True
        print("A listában van prímszám.")
        
if vanebenneprim == True:
    print("Van benne prímszám.")
else:
    print("Nincs benne prímszám.")

# version 2
primdb = 0
for i in range(10):
    if(prime(lista[i])):
        primdb = primdb + 1
print("A listában ",primdb," prímszám van.", sep = '')

if primdb > 0:
    print("Van benne prímszám.")
else:
    print("Nincs benne prímszám.")
    