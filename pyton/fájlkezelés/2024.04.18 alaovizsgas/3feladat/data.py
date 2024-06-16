class CBadás:
    def __init__(self,sor:str) -> None:
        adatok=sor.split(';')
        self.ora=int(adatok[0])
        self.perc=int(adatok[1])
        self.darab=int(adatok[2])
        self.nev=adatok[3]
