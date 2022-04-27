class Eladott:
    ules: int
    tol: int
    ig: int
    
def __init__(self, sor: str) -> None:
    adatok = sor.split(" ")
    self.ules = int(adatok[0])
    self.tol = int(adatok[1])
    self.ig = int(adatok[2])


f = open("eladott.txt", "r")
f.readline()

osszesEladott: list[Eladott] = []

for sor in f:
	egyEladott = Eladott
	osszesEladott.append(egyEladott)

print(len(osszesEladott))