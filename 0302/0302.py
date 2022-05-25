import random

mondat = input("Adjon meg egy mondatot: ")
mondat2 = input("Adjon meg egy másik mondatot: ")
# Melyik mondat hosszabb?
if len(mondat) > len(mondat2):
    print("Az első mondat hosszabb.")
else:
    print("A második mondat hosszabb.")
# Mindkét mondat pontra végződik?
print(mondat.endswith(".") and mondat2.endswith("."))
# Mindkét mondat nagybetűvel kezdődik.
print(mondat == mondat.capitalize() and mondat2 == (mondat.capitalize()))


# DOLGOZAT FELADATA:
szoveg = "A számítógép-programozás (vagy egyszerűen programozás) egy vagy több absztrakt algoritmus megvalósítását jelenti egy bizonyos programozási nyelven.         "
# 1.
print(szoveg.find("-"))
# 2.
print(szoveg.isalpha())
# 3.
szavak = szoveg.split(" ")
print(szavak)
# 4.
print(szoveg.rstrip(" "))
# 5.
print(szoveg.join("Wikipédia"))

# Függvény, ami paraméterként kap egy számot, majd random legenerál egy annyi számból álló listát és kiírja
szam = int(input("Mennyi szám legyen a listába? "))
def szamlistavalami(szam: int) -> int:
    lista = []
    for i in range(szam):
        lista.append(random.randint(0,50))
    print(lista)

szamlistavalami(szam)