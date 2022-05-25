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
f.readline()

# Nobel-díjas emberek neve
for sor in f:
    #print(sor.strip())
    egyEmber = NobelDijasok(sor)
    print("Név: ",egyEmber.nev)

# Hány Nobel-díjas van?

f.seek(0,0)
f.readline()

nobelCount = 0

for sor in f:
    nobelCount += 1

print("\n\nEnnyi Nobel-díjas van: ",int(nobelCount),"\n")

# Hány magyar Nobel-díjas van?

f.seek(0,0)
f.readline()

magyarCount = 0

for sor in f:
    orszagKod = NobelDijasok(sor.strip())
    if orszagKod.orszagkod == "H":
        magyarCount += 1

print(magyarCount," magyar Nobel-díjas szerepel a listában.\n",sep='')

# Mikor kapták az első Nobel-díjat?

f.seek(0,0)
f.readline()

evszamok = []

for sor in f:
    nobelEv = NobelDijasok(sor)
    evszamok.append(int(nobelEv.ev))

print("Az első Nobel-díjat ",min(evszamok),"-ben adták ki.\n",sep='')

# Szerepel-e a listában Otto nevű ember?

f.seek(0,0)
f.readline()

for sor in f:
    egyEmber = NobelDijasok(sor)
    if "Otto" in egyEmber.nev:
        print("Szerepel Otto nevű ember a listában.\n")
        
f.seek(0,0)
f.readline()

szerepele = False

for sor in f:
    egyEmber = NobelDijasok(sor.strip())
    if ("Otto" in egyEmber.nev):
        szerepele = True
        
if (szerepele):
    print("Szerepel Otto nevű ember a listában.\n\n")
else:
    print("Nem szerepel Otto nevú ember a listában. \n\n")

# Írasd ki soronként hány éves korában halt meg a díjazott. ( Ha még él, ne írj ki semmit.)

f.seek(0,0)
f.readline()

for sor in f:
    egyAdat = NobelDijasok(sor)
    szulHal = egyAdat.szul_hal.strip().split("-")
    if szulHal[1] != "":
        kor = int(szulHal[1]) - int(szulHal[0])
        print("Neve: ",egyAdat.nev,"; életkora: ",kor,sep='')