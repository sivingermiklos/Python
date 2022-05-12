# fájl megnyitása ------------------------------------------------------
file = open('orvosi_nobeldijak.txt', 'r', encoding='utf-8')

# lista létrehozása a sorok számára ------------------------------------
lista = []

# első sor beolvasása (fejléc, nem csinálunk vele semmit) --------------
file.readline()

# fájl sorainak bejárása -----------------------------------------------
for sor in file:
    lista.append(sor.strip().split(";"))

# 1. feladat: Hány brit Nobel-djías volt? ------------------------------

print("\n----------1. feladat----------")

gb = 0
for sor in lista:
    if sor[3] == "GB":
        gb += 1
        
print(gb)

# 2. feladat: Hány Nobel-díjas volt 1905 előtt? ------------------------

print("\n----------2. feladat----------")

elott = 0
for sor in lista:
    if int(sor[0]) < 1905:
        elott += 1
        
print(elott)

# 3.feladat: Írasd ki az "A"-val kezdődő neveket! ----------------------

print("\n----------3. feladat----------")


for sor in lista:
    if sor[1].startswith("A"):
        print(sor[1])

# 4. feladat: Kik élnek még és hány évesek? ----------------------------

print("\n----------4. feladat----------")

for sor in lista:
    if len(sor[2]) == 5:
        hanyeves = 2022 - int((sor[2].replace("-","")))
        print(sor[1],hanyeves,"éves")
