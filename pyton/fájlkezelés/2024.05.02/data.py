class versenyzo:
    def __init__(self,sor:str) -> None:
        adatok=sor.split(';')
        self.nev=adatok[0]
        self.szuletesi_ev=int(adatok[1])
        self.rajtszam=int(adatok[2])
        self.neme=adatok[3]
        self.kategoria=adatok[4]
        self.ido_uszas=adatok[5]
        self.ido_elsodepo=adatok[6]
        self.ido_kerekpar=adatok[7]
        self.ido_masodikdepo=adatok[8]
        self.ido_futas=adatok[9]

        self.osszido=self.ido_konvertal(self.ido_uszas)+self.ido_konvertal(self.ido_elsodepo)+self.ido_konvertal(self.ido_kerekpar)+self.ido_konvertal(self.ido_masodikdepo)+self.ido_konvertal(self.ido_futas)


    def ido_konvertal(self,ido:str)->int: #az idő másodpercben
        #00:24:03
        ido_adatok=ido.split(':') # szétdaraboljuk a : karakter mentén
        return int(ido_adatok[0])*3600+int(ido_adatok[1])*60+int(ido_adatok[2])
