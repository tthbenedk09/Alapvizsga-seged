from data import Festmeny

festmenyek:list[Festmeny]=[]

def beolvas(fajlnev:str):
    f=open(fajlnev,'r',encoding='UTF8')
    f.readline()
    for sor in f:
        festmenyek.append(Festmeny(sor.strip()))
    f.close()

def festmenyekSzama()->int:
    return len(festmenyek)    

def festoFestmenyeinekSzama(nev:str)->int:
    db=0
    for festmeny in festmenyek:
        if festmeny.festo==nev:
            db+=1
    return db

def legdragabbKep()->Festmeny:
    legdragabb=festmenyek[0]
    for festmeny in festmenyek[1:]:
        if festmeny.becsultAr>legdragabb.becsultAr:
            legdragabb=festmeny
    return legdragabb # ez egy osztálypéldány minden adatával

def vanE()->bool:
    for festmeny in festmenyek:
        if festmeny.becsultAr<=festmeny.eredetiAr:
            return True
    return False