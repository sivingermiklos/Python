from playsound import playsound
# a Kutya osztály létrehozás

class Kutya:
    nev: str
    fajta: str
    szulIdo: str
    
    def __init__(self, neve: str, fajtaja: str, szulIdeje: int) -> None:
        self.nev = neve
        self.fajta = fajtaja
        self.szulIdo = szulIdeje
    
    def ugat(self):
        print("Vau vau...")
        playsound("D:/.suli/prgy/Python 2022/0324/bark.mp3")
        
# Kutya osztályú objektumok létrehozása (példányosítás) -> 1 konkrét kutya
enKutyam = Kutya("Bákszi","puli",2006)
print("Kutyám neve:",enKutyam.nev)
print("Kutyám fajtája:",enKutyam.fajta)
print("Kutyám születési éve:",enKutyam.szulIdo)
print("Kora:",2022 - enKutyam.szulIdo)

teKutyad = Kutya("Molyma","tacskó",2020)
print("A kutyád neve: ",teKutyad.nev,"; kutyád fajtája: ",teKutyad.fajta,"; kutyád születési éve: ",teKutyad.szulIdo,sep='')

# a Kutya osztály metódusának hívása
enKutyam.ugat()