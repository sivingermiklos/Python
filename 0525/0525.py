from xmlrpc.client import boolean

# OSZTÁLY:

class Haromszog:
    a: int
    b: int
    c: int
    
    # konstruktor
    def __init__(self, sorom) -> None:
        self.a = int(sorom[0])
        self.b = int(sorom[1])
        self.c = int(sorom[2])    
        
    # osztály metódusa: szöveggel visszatérve megmondja, hogy a számok háromszöget alkotnak-e    
    def haromszoge(self) -> str:
        if self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b:
            return "Háromszöget alkotnak"
        else:
            return "Nem alkotnak háromszöget."

    # osztály metódusa: egész számként visszaadja a háromszög kerületét
    def kerulet(self)-> int:
        return self.a + self.b + self.c
    
    def derekszogue(self) -> boolean:
        return self.a^2 +self.b^2 == self.c^2

    def vanEBenne(self, szam: int) -> boolean:
        return szam == self.a or szam == self.b or szam == self.c

f = open("haromszog.txt", "r" ,encoding="utf-8")

lista = []

f.readline()

for sor in f:
    lista.append(sor.strip().split("*"))
print(lista)


for item in lista:
    print(item)
    egyHaromszog = Haromszog(item)
    print(egyHaromszog.haromszoge())
    print("Háromszög kerülete:",egyHaromszog.kerulet())

print(lista)

# 1. feladat: Kérj be a felhasználótól 3 számot (megfelelő adatszerkezetben),
# majd írd ki neki, hogy háromszöget alkotnak-e!
print("\n----------1. feladat----------")
haromszoglista = []

for i in range(3):
    szam = int(input("Add meg a háromszög oldalát: "))
    haromszoglista.append(szam)
teljesharomszog = Haromszog(haromszoglista)
print(teljesharomszog.haromszoge())
print(teljesharomszog.derekszogue())

egySzam = int(input("Adj meg egy számot: "))
print(teljesharomszog.vanEBenne(egySzam))


