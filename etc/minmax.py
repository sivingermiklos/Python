szam1 = int(input("1. szám: "))
szam2 = int(input("2. szám: "))

if szam1 == szam2:
    print("A két szám egyenlő.")
else:
    print("A legkisebb szám: ",min(szam1,szam2))
    print("A legnagyobb szám: ",max(szam1,szam2))