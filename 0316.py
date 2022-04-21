fajl = open("susibaki.txt", "a", encoding='utf-8')
fajl.write("susi gagi" + "\n")
fajl.write("...kövi sor"+"\n")
    
fajl = open("susibaki.txt", "r", encoding='utf-8')
print(fajl.read())
fajl.close()

goloktxt = open("golok.txt","r")
golok2 = open("golok2.txt","w")
goloktxt.readline()
for sor in goloktxt:
    golok2.write(sor)

goloktxt.close()
golok2.close()

goloktxt = open("golok.txt","r")
golok3 = open("golok3.txt","w")
goloktxt.readline()
for sor in goloktxt:
    if int(sor) % 2 == 0 and int(sor) != 0:
        golok3.write(str(sor))

# Bekérek egy mondatot -> fájlba elmentem a mondatot -> minden második szót elmentem

mondatInput = input("Írj le egy mondatot! ")
mondattxt = open("mondat.txt","w",encoding='utf-8')
mondattxt.write(mondatInput)
mondattxt.close()
mondattxt = open("mondat.txt","r",encoding='utf-8')
mondatKiolvasott = mondattxt.readline().strip()
szavakListaja =mondatKiolvasott.split(" ")  
eredmeny = open("eredmeny.txt","w",encoding='utf-8')

for i in range(len(szavakListaja)):
    if i % 2 != 0:
        print(szavakListaja[i])
        eredmeny.write(szavakListaja[i] + " \n")