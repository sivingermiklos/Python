import math

a = (input("Írd be, hogy amogus: "))

def kagi():
    if a == "amogus":
        print("jóóóóóó")
    else:
        print("róóóósz")
        a
    
kagi()
print()
    
# Bekérem a felhasználó nevét
nev = input("Mi a neved? ")

# Funkció, amely üdvözli a megadott nevű embert
def udvozlet(valaki):
    print("Helló, " + valaki)
    
# udvozlet funkció lehívása
udvozlet(nev)

# Funkció, amely megduplázza a bekért számot
def dupla(x):
    print(2*x)

# Bekérek egy véletlenszerű számot a felhasználótól
x = int(input("Adj meg egy véletlenszerű számot: "))

# dupla funkció lehívása
dupla(x)

# Bekérem a két oldal hosszát
teglalapA = int(input("Add meg a téglalap A oldalát: "))
teglalapB = int(input("Add meg a téglalap B oldalát: "))

# Téglalap kerületének kiszámítása (funkcióban)
def teglalapkerulet(teglalapA,teglalapB):
    print(2*teglalapA+2*teglalapB)
 
# teglalapkerulet funkció lehívása   
teglalapkerulet(teglalapA,teglalapB)

# Téglalap területének kiszámítása (funkcióban)
def teglalapterulet(teglalapA,teglalapB):
    print(teglalapA*teglalapB)

# teglalapterulet funkció lehívása   
teglalapterulet(teglalapA,teglalapB)


# Bekérem a kör sugarát
sugar = int(input("Add meg a kör sugarár (r):"))

# Kör kerületének kiszámítása (funkcióban)
def korkerulet(sugar):
    print(2*sugar*math.pi)

# korkerulet funkció lehívása
korkerulet(sugar)

# Kör területének kiszámítása (funkcióban)
def korterulet(sugar):
    print(pow(sugar, 2)*math.pi)

#korterulet funkció lehívása    
korterulet(sugar)