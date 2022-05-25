# sorok nevű üres lista létrehozása
sorok = []

# file nevű, fájl típusú változó létrehozása olvasásra, UTF-8-as kódolással
file = open('forras.txt', 'r', encoding='utf-8')

# for ciklussal végigmegyek a sorokon
# a ciklusban minden sort hozzáfűzök a listához
for e in file:
    sorok.append(e.strip())

# Kiíratom a sorok nevű listámat
print(sorok)
file.close()

# FELADAT: txt -> nevek; írassuk ki egymás után a neveket.

f = open('nevek.txt', 'r', encoding='utf-8')
nev1 = f.readline().strip()
print(nev1)
nev2 = f.readline().strip()
print(nev2)
nev3 = f.readline().strip()
print(nev3)
f.close()


# FELADAT 2: txt -> számok; adjuk hozzá egy "szamok" nevű listához a txt-ben található számokat.
szamok = []
fajl = open('szamok.txt', 'r')
for e in fajl:
    szamok.append(int(e.strip()))
print(szamok)
fajl.close()