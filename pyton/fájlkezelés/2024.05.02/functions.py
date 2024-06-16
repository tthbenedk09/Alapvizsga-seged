from data import versenyzo
import math

versenyzok:list[versenyzo]=[]

def beolvas(fajlnev:str):
    f=open(fajlnev,'r',encoding='utf8')
    for sor in f:
        versenyzok.append(versenyzo(sor.strip()))
    f.close()

def versenyzok_szama()->int:
    return len(versenyzok)

def kategoria_letszam(kategoria:str)->int:
    letszam=0
    for versenyzo in versenyzok:
        if versenyzo.kategoria==kategoria:
            letszam+=1
    return letszam

def atlag_eletkor(ev:int)->float:
    osszeg=0
    for versenyzo in versenyzok:
        eletkor=ev-versenyzo.szuletesi_ev
        osszeg+=eletkor
        #osszeg+=ev-versenyzo.szuletesi_ev
    return osszeg/versenyzok_szama()        
    #return osszeg/len(versenyzok)     

def kategoria_rajtszamok(kategoria:str)->list:
    kategoria_lista=[]
    for versenyzo in versenyzok:
        if versenyzo.kategoria==kategoria:
            kategoria_lista.append(versenyzo.rajtszam)
    return kategoria_lista

def gyoztes(nem:str)->versenyzo:
    gyoztes_ideje=math.inf #+végtelen
    gyoztes_versenyzo=None
    for versenyzo in versenyzok:
        if versenyzo.neme==nem and versenyzo.osszido<gyoztes_ideje:
            gyoztes_ideje=versenyzo.osszido
            gyoztes_versenyzo=versenyzo
    return gyoztes_versenyzo

    