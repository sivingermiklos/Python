import math

# 1. feladat:
# Kérjen be a program 2 számot, és írja ki, hogy melyik nagyobb, melyik kisebb. Azt is írja ki, ha egyenlőek.

#                   Bekérünk a felhasználótól két számot.
szam1 = int(input("Adj meg egy számot: "))
szam2 = int(input("Adj meg mégegy számot: "))

#                   Ha az első szám nagyobb, mint a második szám, akkor írassa ki, hogy az első szám a nagyobb.
if (szam1 > szam2):
    print("Az első szám a nagyobb. ",szam1,">",szam2)
#                   Ha a második szám nagyobb, mint az első szám, akkor írassa ki, hogy a második szám a nagyobb.
elif (szam1 < szam2):
    print("A második szám a nagyobb.",szam1,"<",szam2)
#                   Ha egyik állítás sem igaz, akkor kiíratja, hogy a két szám egyenlő.
else:
    print("A két szám egyenlő.",szam1,"=",szam2)

# 2. feladat:
# Kérd be egy háromszög oldalait, majd határozd meg és írd ki, hogy a háromszög megszerkeszthető-e!
# (A háromszög akkor megszerkeszthető, ha bármely két oldalának az összege nagyobb mint a harmadik oldal.)

#                   Bekérünk a felhasználótól a háromszög három oldalát.
haromszog1 = int(input("Add meg a háromszög első oldalát: "))
haromszog2 = int(input("Add meg a háromszög második oldalát: "))
haromszog3 = int(input("Add meg a háromszög harmadik oldalát: "))

#                   Ha a két oldal összege nagyobb, mint a harmadik oldal, akkor kiíratja azt, hogy a háromszög megszerkeszthető.
if (haromszog1 + haromszog2 > haromszog3) and (haromszog1 + haromszog3 > haromszog2) and (haromszog2 + haromszog3 > haromszog1):
    print("A háromszög megszerkeszthető.")
#                   Ha nem nagyobb a két oldal összege a harmadik oldalnál, akkor a háromszög nem megszerkeszthető.
else:
    print("A háromszög nem megszerkeszthető!")

# 3. feladat:
# Kérd be egy háromszög oldalait, majd számold ki a kerületét, és az alábbi képlettel a területét is:
# s = Kerület/2
# Terület = Gyök(s * (s-a) * (s-b) * (s-c))

#                   A felhasználótól bekérjük a háromszög oldalait.
haromszogA = int(input("Add meg a háromszög első oldalát: "))
haromszogB = int(input("Add meg a háromszög második oldalát: "))
haromszogC = int(input("Add meg a háromszög harmadik oldalát: "))

#                   Változókban eltároljuk a kerületet, területet.
haromszogKerulet = haromszogA + haromszogB + haromszogC
s = haromszogKerulet / 2
haromszogTerulet = math.sqrt(s * (s - haromszogA) * (s - haromszogB) * (s - haromszogC))

#                   Kiíratom a háromszög kerületét, területét.
print("A háromszög kerülete: ",haromszogKerulet)
print("A háromszög területe: ",haromszogTerulet)

# 4. feladat:
# Kérd be egy téglalap oldalait és tárolja őket VALÓS típusú változókba, majd határozd meg, a téglalap területét és kerületét!
# A területet és a kerületet a következő képletekkel számold:
# T = a * b
# K = 2 * (a + b)


#                   Bekérünk a felhasználótól a téglalap 2 oldalát.
teglalapA = float(input("Add meg a téglalap első oldalát: "))
teglalapB = float(input("Add meg a téglalap második oldalát: "))

#                   Eltároljük a téglalap kerületét, területét valós változókba.
teglalapTerulet = teglalapA * teglalapB
teglalapKerulet = 2 * (teglalapA + teglalapB)

#                   Kiíratom a téglalap kerületét, területét.
print("A téglalap kerülete: ",teglalapKerulet)
print("A téglalap területe: ",teglalapTerulet)
