import math
from xmlrpc.client import boolean

#FELADAT: Készítsünk egy olyan függvényt, ami kiszámolja a kúp térfogatát.
# korSugar - korMagassag = kupTerfogat
korSugar = int(input("Add meg a kör sugarát: "))
korMagassag = int(input("Add meg a kör magasságágt: "))

def kupTerfogat(korSugar: int, korMagassag: int) -> float:
    return pow(korSugar,2)*math.pi*korMagassag/3
print(kupTerfogat(korSugar,korMagassag))

# FELADAT 2: A szökőév meghatározásához készítsünk egy saját függvényt!

ev = int(input("Add meg az évszámot: "))

def szokoEv(ev: int) -> boolean:
    if ev % 400 == 0 or ev % 4 == 0 and ev % 100 != 0:
        return True
    else:
        return False
print(szokoEv(ev))

# 1 soros verzió
def szokoEvV2(ev: int) -> boolean:
    return ev % 400 == 0 or ev % 4 == 0 and ev % 100 != 0
print(szokoEvV2(ev))
        
        
# FELADAT 3: 2 évszám közötti szökőévek kiíratása.
db = 0

evTol = int(input("Add meg az első évszámot: "))
evIg = int(input("Add meg a második évszámot: "))
lista = []
for i in range(evTol,evIg + 1):
    if szokoEv(i):
        print(i)
        db = db + 1

if (db == 0):
    print("Nem volt szökőév a két megadott év között.")