f = open("ub2017egyeni.txt",'r',encoding='utf-8')

# Eredmeny nevű osztály létrehozása 
class Eredmeny:
    nev: str
    rajtszam: int
    kategoria: str
    ido: str
    tavSzazalek: int
    
    def  __init__(self, sor: str) -> None:
        adatok = sor.split(';')
        self.nev = adatok[0]
        self.rajtszam = int(adatok[1])
        self.kategoria = adatok[2]
        self.ido = adatok[3]
        self.tavSzazalek = int(adatok[4])

f.readline()
for sor in f:
    # összes sor kiiratása:
    #print(sor.strip())
    # egyAdat nevű Eredmeny típusú objektum létrehozása
    egyAdat = Eredmeny(sor)
    print("Neve: ",egyAdat.nev,"; ideje: ",egyAdat.ido,sep='')
    
f.seek(0.0)
f.readline()
noiCount = 0
for sor in f:
    egyAdat = Eredmeny(sor)
    if egyAdat.kategoria == "Noi":
        noiCount += 1
        
print("Női versenyzők száma: ",noiCount,sep='')

f.seek(0.0)
f.readline()
szazalek = []
for sor in f:
    egyAdat = Eredmeny(sor)
    szazalek.append(int(egyAdat.tavSzazalek))
print(min(szazalek))
    