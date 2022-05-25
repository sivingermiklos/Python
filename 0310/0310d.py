from xmlrpc.client import boolean

# 1. feladat:

num1 = int(input("Első szám: "))
num2 = int(input("Második szám: "))
num3 = int(input("Harmadik szám: "))

def pozitivE(num1: int, num2: int, num3: int) -> boolean:
    if num1 >= 0 and num2 >= 0 and num3 >= 0:
        return True
    else:
        return False
    
print(pozitivE(num1,num2,num3))

if pozitivE(num1,num2,num3) == True:
    print("Aktuális paraméternek azt nevezünk, amikor ---")
else:
    print("\ndef függvény_neve(formális parametérlista) -> visszatérési_értek:")
