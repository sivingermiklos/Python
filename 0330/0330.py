be = open("haromszogek.txt","r")
sorok = []
for sor in be:
    sorok = sor.strip().split(" ")
    print(sorok)
be.seek(0.0)
be.readline()
print("2. sor: ",be.readline())

harmadiksor = be.readline().strip().split(" ")
print(harmadiksor)
print(max(harmadiksor))
print(harmadiksor[1])

ki = open("ki.txt","w",encoding="utf-8")
ki.write(harmadiksor[1])


be.seek(0.0)
for i in range(4):
    print(be.readline().strip())