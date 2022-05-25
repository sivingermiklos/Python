import math
from xmlrpc.client import boolean
# FELADAT: Kérj be a felhasználótól egy számot!
# Ennyiszer írd ki a képernyőre, hogy "Hello World!"
# A kiíratást függvénnyel oldd meg, ami paraméterként a megadott számot kapja.
# A függvény visszaadott értéke az legyen, hogy a szám páros-e vagy sem.

szam = int(input("Adj meg egy számot: "))

def kiiratas(szam: int) -> boolean:
    for i in range(szam):
        print("Hello world!")
    return szam % 2 == 0
    
print(kiiratas(szam))

# FELADAT 2: Kérd be a felhasználótól egy derékszögű háromszög a és b oldalát!
# A 2 számot egy függvénykapja meg paraméterként. A visszaadott érték a c oldal hossza legyen.

a = int(input("Egyik oldal: "))
b = int(input("Másik oldal: "))

def pit(a: int, b: int) -> int:
    c = pow(a,2) + pow(b,2)
    return math.sqrt(c)

print(pit(a,b))

# FELADAT 3: Írj egy Python eljárást, amely paraméterként kap egy szót (stringet)
# és annyi darab csillag (*) karaktert ír ki a képernyőre, ahány karaktert
# tartalmaz a szó! A programodban hívd is meg ezt az alprogramot!

szo = input("Adj meg egy szót: ")
def szo2csillag(szo):
    for i in range(len(szo)):
        print("*", end="")
szo2csillag(szo)

# FELADAT 4: Írj egy Python függvényt, amely paraméterként kap 2 egész számot
# és visszatér a két szám álal meghatározott zárt intervallumban található
# egész számok összegével! A programodban hívd is meg ezt az alprogramot 
s1 = int(input("Első szám: "))
s2 = int(input("Második szám: "))
def szamosfeladat(szamok: int) -> int:
    szamok = range(s1 + 1,s2)
    for f in szamok:
        print(f)

szamosfeladat(szamok)