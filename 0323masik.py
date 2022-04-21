from xmlrpc.client import boolean

def nincsoszthato(sor: str) -> boolean:
    szamok = []
    szamok = sor.strip().split(";")
    for i in range(len(szamok)):
        if(int(szamok[i]) % 3 == 0):
            return False
    return True
f = open("forras2.txt","r")
for sor in f:
    if nincsoszthato(sor):
        print(sor)