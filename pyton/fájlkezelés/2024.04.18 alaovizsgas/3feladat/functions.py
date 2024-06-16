from data import CBadás

cbAdasok:list[CBadás]=[]

def beolvas(fajlnev:str):
    f=open(fajlnev,'r',encoding='utf8')
    f.readline()
    for sor in f:
        cbAdasok.append(CBadás(sor.strip()))
    f.close()

def bejegyzesek_szama():
    return len(cbAdasok) 

def nev_bejegyzesSzam(nev:str): #névhez tartozó bejegyzések száma
    db=0
    for adas in cbAdasok:
        if adas.nev==nev:
            db+=1
    return db

def maxAdasDb(): # azt mondja meg, hogy mennyi volt az 1 percen belüli legtöbb adás
    max=0
    for adas in cbAdasok:
        if adas.darab>max:
            max=adas.darab
    return max

def fajlbaIras(fajlnev:str):
    f=open(fajlnev,'w',encoding='utf8')
    f.write('Kezdes;Nev;AdasDb\n')
    for adas in cbAdasok:
        f.write(f'{adas.ora*60+adas.perc};{adas.nev};{adas.darab}\n')
    f.close()
