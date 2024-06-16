class Festmeny:
    def __init__(self,sor:str) -> None:
        adatok=sor.split(';')
        self.festmeny=adatok[0]
        self.festo=adatok[1]
        self.keszitesEve=int(adatok[2])
        self.becsultAr=int(adatok[3])
        self.eredetiAr=int(adatok[4])
        self.eladasEve=int(adatok[5])