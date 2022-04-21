# FELADAT: Írj egy függvényt, ami kap 3 számot 
# paraméterenként, és a visszaadja a legnagyobbat!

from xmlrpc.client import boolean
import random

a = random.randint(0,30)
b = random.randint(0,30)
c = random.randint(0,30)
print(a,b,c)
def legnagyobbSzam(a: int, b: int, c: int) -> int:
    if (a > b and a > c):
        print("Az 1. szám a legnagyobb.")
    elif (b > a and b > c):
        print("A 2. szám a legnagyobb.")
    else:
        print("A 3. szám a legnagyobb.")
        

legnagyobbSzam(a, b, c)

# FELADAT: Írj egy logikai értékkel visszatérő Python függvényt, amely 
# paraméterenként kap három számot és eldönti, hogy az összes paramétere pozitív-e!

szam1 = int(input("Add meg az első számot: "))
szam2 = int(input("Add meg az második számot: "))
szam3 = int(input("Add meg az harmadik számot: "))
def pozitivSzam(szam1: int, szam2: int, szam3: int) -> boolean:
    if (szam1 >= 0 and szam2 >= 0 and szam3 >= 0):
        return True
    else:
        return False

print(pozitivSzam(szam1,szam2,szam3))

# FELADAT: Írj egy Python eljárást, amely paraméterenként kap 2 egész számot (N és M) 
# és kiírja a képernyőre a csillag (*) karaktereket M darab sorban és N darab oszlopban
# (tehát NxM darab karaktert egy téglalap alakú képernyőrészre)!

nOszlop = int(input("Add meg, hogy mennyi oszlop legyen: "))
mSor = int(input("Add meg, hogy mennyi sor legyen: "))
def csillag(nOszlop: int,mSor: int):
    for i in range(nOszlop):
        for i in range(mSor):
            print("*", end='  ')
        print()
csillag(nOszlop,mSor)
