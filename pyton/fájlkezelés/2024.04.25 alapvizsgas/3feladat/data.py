class Épület:
    def __init__(self,sor:str) -> None:
        adatok=sor.split(';')
        self.nev=adatok[0]
        self.varos=adatok[1]
        self.orszag=adatok[2]
        self.magassag=float(adatok[3].replace(',','.'))
        self.emeletek=int(adatok[4])
        self.epult=int(adatok[5])