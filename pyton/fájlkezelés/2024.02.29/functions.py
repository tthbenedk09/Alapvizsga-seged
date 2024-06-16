from data import Eredmeny

eredmenyek:list[Eredmeny]=[]

def fajlBeolvas(fajlnev):
    f=open(fajlnev,'r',encoding='utf8')
    for sor in f:
        eredmenyek.append(Eredmeny(sor))
    f.close()

def helyezesekSzama(helyezes)->int:
    db=0
    for e in eredmenyek:
        if e.helyezes==helyezes:
            db+=1
    return db

def osszPont()->int:
    osszeg=0
    for e in eredmenyek:
        osszeg+=e.pont()
    return osszeg

def sportagErmek(sportag)->int:
    db=0
    for e in eredmenyek:
        if e.sportag==sportag and e.helyezes<=3:
            db+=1
    return db

def fajlbaIras(fajlnev):
    f=open(fajlnev,'w',encoding='utf8')
    for e in eredmenyek:
        if e.sportag=='kajakkenu':
            f.write(f'{e.helyezes} {e.letszam} {e.pont2()} kajak-kenu {e.versenyszam}\n')
        else:
            f.write(f'{e.helyezes} {e.letszam} {e.pont2()} {e.sportag} {e.versenyszam}\n')
    f.close()

def maxLetszam()->Eredmeny:
    legtobb=eredmenyek[0]
    for e in eredmenyek[1:]:
        if e.letszam>legtobb.letszam:
            legtobb=e
    return legtobb