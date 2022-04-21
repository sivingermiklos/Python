from xmlrpc.client import boolean

# Változók megadása
a = ""
osszege = 0
talalatok = []
# Írj egy függvényt, ami egy paraméterként kapott számról eldönti, hogy 0 és 100 közötti 3-mal osztható páros szám-e.
def feladat(szam) -> boolean:
    if szam < 100 and szam > 0 and szam % 3 == 0 and szam % 2 == 0:
        return True
    return False
# A felhasználótól egész számokat kér be addig, amíg 0-t nem ad meg. Amint megadja a számot, vizsgáld meg a függvény segítségével, 
# hogy az előző feltétel teljesül-e rá. Ha igen, add hozzá egy 'talalatok' nevű listához.
while a != 0:
    a = int(input("Adj meg egy számot: "))
    if feladat(a):
        talalatok.append(a)
for i in range(len(talalatok)):
    osszege = osszege + talalatok[i]
# Az eredmények kiíratása
print("A függvény ennyi számot dolgozott fel: ",(len(talalatok)), sep='')
print("A lista összege: ", osszege, sep='')
print("A lista számainak átlaga: ", osszege / len(talalatok), sep='')