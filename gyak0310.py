
# 2. feladat: 

golok = []
osszGolok = 0

goloktxt = open("golok.txt", 'r', encoding='utf-8')
goloktxt.readline()
for i in range(5):
    golok.append(int(goloktxt.readline()))

print(golok)

for e in range(len(golok)):
    osszGolok += golok[e]
    
atlag = osszGolok / len(golok)
print("Összes gól: ",osszGolok)
print("A gólok meccsenkénti átlaga: ",atlag)
if osszGolok <= 2:
    print("gyenge")
elif osszGolok <= 5:
    print("közepes")
elif osszGolok >= 6:
    print("kiváló")