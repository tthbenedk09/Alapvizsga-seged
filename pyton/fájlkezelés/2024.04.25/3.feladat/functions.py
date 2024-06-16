from data import Épület

epuletek:list[Épület]=[]

def beolvas(fajlnev:str):
    f=open(fajlnev,'r',encoding='utf8')
    f.readline()
    for sor in f:
        epuletek.append(Épület(sor.strip()))
    f.close()

def epuletek_szama():
    return len(epuletek)

def emeletek_osszege():
    osszeg=0
    for epulet in epuletek:
        osszeg+=epulet.emeletek
    return osszeg

def legmagasabb_epulet():
    legmagasabb=epuletek[0]
    for epulet in epuletek[1:]:
        if epulet.magassag>legmagasabb.magassag:
            legmagasabb=epulet
    return legmagasabb

def van_orszag(orszag:str):
    for epulet in epuletek:
        if epulet.orszag==orszag:
            return True
    return False