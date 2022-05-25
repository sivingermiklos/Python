class NobelDijasok:
    ev: int
    nev: str
    szul_hal: str
    orszagkod: str
    
    def __init__(self, sor: str) -> None:
        adatok = sor.split(";")
        self.ev = int(adatok[0])
        self.nev = adatok[1]
        self.szul_hal = adatok[2]
        self.orszagkod = adatok[3]
    
f = open("orvosi_nobeldijak.txt","r",encoding='utf-8')

# Üres objektumlista létrehozása
# Ez egy olyan lista, ami sok NobelDijasok típusú objektumot tartalmaz
osszesNobelDijas: list[NobelDijasok] = []

f.readline()
for sor in f:
    egyEmber = NobelDijasok(sor.strip())
    osszesNobelDijas.append(egyEmber)
    
print(osszesNobelDijas[10].nev)

for egy in osszesNobelDijas:
    print(egy.ev)
for i in range(len(osszesNobelDijas)):
    print(osszesNobelDijas[i].nev)