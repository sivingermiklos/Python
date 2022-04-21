from xmlrpc.client import boolean

haromszogektxt = open("haromszogek.txt","r")
szamok = []

def haromszogek(a: int, b: int, c: int) -> boolean:
    return (a + b > c and a + c > b and b + c > a)
    
for sor in haromszogektxt:
    szamok = sor.strip().split(" ")
    print(haromszogek(int(szamok[0]),int(szamok[1]),int(szamok[2])))