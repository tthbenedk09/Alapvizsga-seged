class Varos:
    def __init__(self,sor:str) -> None:
        adatok=sor.strip().split(';')
        self.nev=adatok[0]
        self.orszag=adatok[1]
        self.lakossag=int(adatok[2])

    def szokozokDb(self)->int:
        db=0
        for karakter in self.nev:
            if karakter==' ':
                db+=1
        return db