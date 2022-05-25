f = open("ub2017egyeni.txt", 'r', encoding='utf-8')
f.readline()

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

# 1. Írassa ki, hány induló volt!
# -------------------------------------------------------------------------------------------------------
print("\n-----------1. feladat-----------\n")

osszesEredmeny: list[Eredmeny] = []
# osszesEredmeny = []
for sor in f:
    egyEredmeny = Eredmeny(sor.strip())
    osszesEredmeny.append(egyEredmeny)
print(len(osszesEredmeny),"eredmény van a listában.")


# 2. Számolja meg, hány női sportoló teljesítette a teljes távot!
# -------------------------------------------------------------------------------------------------------
print("\n-----------2. feladat-----------\n")

noiCount = 0

for egyAdat in osszesEredmeny:
    if egyAdat.kategoria == "Noi" and egyAdat.tavSzazalek == 100:
        noiCount += 1

print(noiCount,"női sportoló teljesítette a távot.")


# 3. Kérje be a felhasználótól egy sportoló nevét
#    majd határozza meg s írja ki a minta szerint, hogy a sportoló indult-e a versenyen!
#    Ha a sportoló indult a versenyen, akkor azt is írja ki a képernyőre, hogy a teljes távot teljesítette-e!
# -------------------------------------------------------------------------------------------------------
print("\n-----------3. feladat-----------\n")

sportoloNeve = input("Sportoló neve: ")
bennevane = False
teljesitett = False

for egyAdat in osszesEredmeny:
    if egyAdat.nev == sportoloNeve:
        bennevane = True
        if egyAdat.tavSzazalek == 100:
            teljesitett= True

if bennevane:
    print("Szerepel")
else:
    print("Nem szerepel")

if teljesitett:
    print("Teljesítette")
else:
    print("Nem teljesítette")


# 4. Írassa ki az első sportoló idejét órában!
# -------------------------------------------------------------------------------------------------------
print("\n-----------4. feladat-----------\n")

ido = osszesEredmeny[0].ido.split(":")
oraban = (int(ido[0])*3600 + int(ido[1])*60 + int(ido[2])) / 3600
print("Az első sportoló ideje órában: ",round(float(oraban),2)," óra",sep='')


# 5. Készítsen egy függvényt (idoOraban), ami megkapja a versenyzú időeredményét, majd visszaadja az időt órában!
# -------------------------------------------------------------------------------------------------------
print("\n-----------5. feladat-----------\n")

def idoOraban(idoString: str) -> float:
    ido = idoString.split(":")
    ora = (int(ido[0])*3600 + int(ido[1])*60 + int(ido[2])) / 3600
    return ora
    
for egyAdat in osszesEredmeny:
    print(egyAdat.nev,idoOraban(egyAdat.ido))


# 6. Határozza meg és írja ki a minta szerint a teljes távot teljesítő férfi sportolók átlagos idejét órában!
# -------------------------------------------------------------------------------------------------------
print("\n-----------6. feladat-----------\n")

ferfiDb = 0
osszesIdo = 0

for egyAdat in osszesEredmeny:
    if egyAdat.kategoria == "Ferfi" and egyAdat.tavSzazalek == 100:
        ferfiDb += 1
        osszesIdo += idoOraban(egyAdat.ido)

print("Teljes távot teljesítő férfiak száma:",ferfiDb)
print("Összes idő:",int(osszesIdo))
print("Átlag idő:",int(osszesIdo) / int(ferfiDb))


# 7. Hány célba érkezett versenyző van, aki előtti és utánni versenyző nem teljesítette a távot?
# -------------------------------------------------------------------------------------------------------
print("\n-----------7. feladat-----------\n")

db = 0

for i in range(len(osszesEredmeny)-1):
    if osszesEredmeny[i].tavSzazalek == 100 and osszesEredmeny[i-1].tavSzazalek < 100 and osszesEredmeny[i+1].tavSzazalek < 100:
        db += 1
        
print(db)

