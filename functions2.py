# Függvény: Névvel ellátott, adott feladatot elvégző utasítások sorozata
# A függvényt használatelőtt definiálni/deklarálni kell
# Formája: 
# ===================
# 1.) Függvény fej:
#     def függvény_neve(formális paraméterlista) -> függvény_visszatérési_értékének_a_típusa:
# ===================
# 2.) Függvény törzs:
#     Tetszőleges számú utasítás

from xmlrpc.client import boolean


def osszead(a: int, b: int) -> int:                 # A függvény feje
    # def => függvény definíciót bevezető foglalt kulcsszó
    # osszead => a függvény neve
    # () => operátorok a paraméterek megadására
    # a: int, b: int => függvény formális paraméterei azonosíval és típussal
    # -> => függgvény visszatérési értékét ezután az "operátor" után adhatjuk meg (opcionális)
    # int => a függvény visszatérési értékének a típusa4
    
    return a + b                                    # A függvény törzse
# Függvény hívása
# A hívás szintaxisa:
# Függvény_azonosítója(aktuális paraméterlista)
osszead(3,4)                            # Függvény visszatérési értéke így elveszik
print(osszead(3,4))                     # A függvény visszatérési értékét a képernyőre írjuk
osszeg: int = osszead(3,4)              # A függvény visszatérési értékét eltároljuk
print(osszeg)

# FELADAT: Készítsünk olyan függvényt, amely a 2 szám legnagyobb közös osztóját adja vissza
a = int(input("Adj meg egy számot: "))
b = int(input("Adj meg egy másik számot: "))
def gcd(a: int, b: int) -> int:
    while b:
        a,b = b, a%b
    return a
print("A két szám legnagyobb közös osztója: ",gcd(a,b), sep='')

def lnko(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
print("A két szám legnagyobb közös osztója: ",lnko(a,b), sep='')


# FELADAT: Írj egy logikai (True, False) értékkel vis szatérő Python függvényt, amely
# paraméterenként kap egy egész számot, és eldönti a számról,
# hogy osztható-e 2-vel és 3-mal és egyszerre!
x = int(input("Adj meg egy számot, amely osztható 2-vel és 3-mal is egyszerre: "))
def osztoSzamok(x: int) -> boolean:
    if ( x % 2 == 0 and x % 3 == 0):
        return True
    else:
        return False
print(osztoSzamok(x))