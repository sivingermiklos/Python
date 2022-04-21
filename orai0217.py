#   1. minden szó nagybetűvel kezdődik

mondat = "A Python egy általános célú, magas szintű, interaktív, objektum orientált programozási nyelv, melyet Guido van Rossum holland programozó kezdett el fejleszteni 1989 végén, majd hozott nyilvánosságra 1991-ben."
print(mondat.title())

#   2. eltárolni a fentit egy másik változóban

mondatTitle = mondat.title()
print(mondatTitle)

#   3. milyen karakter van az első vessző előtt?

mondatElsoVesszo = mondat.find(",")
print(mondat[mondatElsoVesszo-1])

#   4. csak betűkből áll a szöveg?

if mondat.isalpha() == False:
    print("A mondatban vannak más karakterek is.")
else:
    print("A mondatban csak betűk vannak.")
    
#   5. a vesszők mentén feldarabolva listába rakni

lista = mondat.split(",")
print(lista)

#   6. Hány eleme van a listának?

print("",(len(lista)), sep='')

#   7. Magas asl kezdődik a lista 2. eleme?

print(lista[1].startswith(" magas"))
    
#   8. Milyen karkater van az utolsó szóköz után?

mondatSzokozUtan = mondat.rfind(" ")
print(mondat[mondatSzokozUtan+1])