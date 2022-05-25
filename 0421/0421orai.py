from xmlrpc.client import boolean


class Focimeccs:
    fordulo: int
    hazaiGol: int
    vendegGol: int
    hazaiFelidoGol: int
    vendegFelidoGol: int
    hazaiCsapat: str
    vendegCsapat: str
    
    def __init__(self, sor: str) -> None:
        adatok = sor.split(" ")
        self.fordulo = int(adatok[0])
        self.hazaiGol = int(adatok[1])
        self.vendegGol = int(adatok[2])
        self.hazaiFelidoGol = int(adatok[3])
        self.vendegFelidoGol = int(adatok[4])
        self.hazaiCsapat = str(adatok[5])
        self.vendegCsapat = str(adatok[6])
        
f = open("meccs.txt", 'r', encoding='utf-8')
f.readline()
osszesEredmeny: list[Focimeccs] = []

# 0. feladat --------------------------------------------------------------------------------
print("\n-----------0. feladat-----------\n")


for sor in f:
    egyMeccs = Focimeccs(sor.strip())
    osszesEredmeny.append(egyMeccs)
print(len(osszesEredmeny))

# 1. feladat --------------------------------------------------------------------------------
print("\n-----------1. feladat-----------\n")


forduloInput = int(input("Forduló száma? (1 és 20 között) "))

for egyAdat in osszesEredmeny:
    if egyAdat.fordulo == forduloInput:
        print(egyAdat.hazaiCsapat,"-",egyAdat.vendegCsapat,": ",egyAdat.hazaiGol,"-",egyAdat.vendegGol," (",egyAdat.hazaiFelidoGol,"-",egyAdat.vendegFelidoGol,")",sep='')

# 2. feladat --------------------------------------------------------------------------------
print("\n-----------2. feladat-----------\n")

csapatnevInput = input("Csapat neve? ")
szerepelE = False

for egyAdat in osszesEredmeny:
    if egyAdat.hazaiCsapat == csapatnevInput or egyAdat.vendegCsapat == csapatnevInput:
        szerepelE = True
        
if szerepelE:
    print(csapatnevInput,"nevű csapat szerepelt a mérkőzéssorozatban.")
else:
    print(csapatnevInput,"nevű csapat nem szerepelt a mérkőzéssorozatban.")

# 3. feladat --------------------------------------------------------------------------------
print("\n-----------3. feladat-----------\n")

nyulakGol = 0

for egyAdat in osszesEredmeny:
    if egyAdat.vendegCsapat == "Nyulak":
        nyulakGol += egyAdat.vendegGol
        
print(nyulakGol)

# 4. feladat --------------------------------------------------------------------------------
print("\n-----------4. feladat-----------\n")

def forditottake(a: int, b: int, c: int, d: int) -> boolean:
    return (c > d and b > a) or (d > c and a > b)

for egyAdat in osszesEredmeny:
    print(forditottake(egyAdat.hazaiGol,egyAdat.vendegGol,egyAdat.hazaiFelidoGol,egyAdat.vendegFelidoGol))