# Írasd ki az összes sort
f = open("adatok.txt","r")

for i in range(6):
    print("Sor: ",f.readline().strip())
    
# Olvasd be a fájl első sorát, amely megadja, hogy összesen hány adatsor van.    
f.seek(0,0)
print("Sorok száma: ",f.readline().strip())

# Írasd ki egy sorokszama.txt fájlba a sorok számát. 
sorokszama = open("sorokszama.txt","w")
f.seek(0,0)
sorokszama.write(f.readline())

# Írasd ki külön az adatsorokat és külön az összes sorok számát.
f.seek(3,0)
for e in range(5):
    print("Sorok száma a 2. sortól: ",f.readline().strip())
    
# a sorokban levő 3 szám szorzatát írd ki. Csak az adatsorokkal dolgozz!
f.seek(0,0)
f.readline()
sorok = []
for g in range(5):
    sorok = (f.readline().strip().split(";"))
    print("Szorzat: ",int(sorok[0]) * int(sorok[1]) * int(sorok[2]))
