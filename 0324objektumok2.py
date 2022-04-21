# Autó nevű osztály létrehozása

class Auto:
    marka: str
    evjarat: int
    szin: str
    hengerUrTartalom: int
    
    def __init__(self, markaja: str, evjarata: int, szine: str, hengerUT: int) -> None:
        self.marka = markaja
        self.evjarat = evjarata
        self.szin = szine
        self.hengerUrTartalom = hengerUT
        
        
    def kocsihang(self):
        print("Vroom vroom...")
        
        
enAutom = Auto("Audi",2020,"fekete",10000)
print("Autóm márkája: ",enAutom.marka,"; autóm évjárata: ",enAutom.evjarat,"; autóm színe: ",enAutom.szin,"; autóm hengerűrtartalma: ",enAutom.hengerUrTartalom,sep='')

enAutom.kocsihang()