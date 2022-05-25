# FELADAT: Írasd ki azokat a sorokat, melyekben nincs 3-mal oszthátó szám.
file = open("haromszogek.txt", "r")
szamok = []

def oszthato(a: int, b: int, c: int):
    if int(a) % 3 != 0 and int(b) % 3 != 0 and int(c) % 3 != 0:
        print(a,b,c)

        
for sorok in file:
    szamok = sorok.strip().split(" ")
    oszthato(int(szamok[0]),int(szamok[1]),int(szamok[2]))