# FELADAT 2: Tölts fel egy listát 10 darab kétjegyű egész számmal!
#            Lista elemeit írja ki a képernyőre.
#            Készíts egy függvényt prime néven, ami eldönti egy számról, hogy prímszám-e.
#            (Egy szám akkor prímszám, ha 1-el és magával osztható, pontosan 2 osztója van.)
#            Döntsd el, hogy a listában van-e prímszám.

import random
from re import A
from tkinter import E
from xmlrpc.client import boolean

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
    
# FELADAT: Készítsünk egy függvényt, ami egy paraméterként megkapott szóban meghatározza a magánhangzók számát.

def maganhangzoCounter(nap: str) -> int:
    db: int = 0
    mgh = "aáeéiíoóöőuúüű"
    for i in range(len(nap)):
        if nap[i] in mgh:
            db = db + 1
    return db

print(maganhangzoCounter("hétfő"))

napok = ["hétfő" , "kedd" , "szerda" , "csütörtök" , "péntek" , "szombat" , "vasárnap"]
for elem in napok:
    print(maganhangzoCounter(elem))
    
maxhely = 0

for i in range (len(napok)):
    if(maganhangzoCounter(napok[i])) > (maganhangzoCounter(napok[maxhely])):
        maxhely = i
        
print(napok[maxhely])