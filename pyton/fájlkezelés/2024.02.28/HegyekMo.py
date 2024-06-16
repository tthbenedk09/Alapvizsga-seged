from hegycsucs import hegycsucs

hegyek:list[hegycsucs]=[] # a hegycsúcs példányokat tároljuk benne

def beolvas(fajlnev):
    f=open(fajlnev,'r',encoding='utf8')
    f.readline()
    for sor in f:
        hegyek.append(hegycsucs(sor.strip()))
    f.close()   

def csucsok_szama()->int: # ha mindent függvénnyel kell megoldani
    return len(hegyek)

def atlag_magassag()->float:
    osszeg=0
    for h in hegyek:
        osszeg+=h.magassag
    return osszeg/csucsok_szama() # len(hegyek) is jó

def legmagasabb_csucs()->hegycsucs:
    legmagasabb=hegyek[0]
    for h in hegyek[1:]:
        if h.magassag>legmagasabb.magassag:
            legmagasabb=h
    return legmagasabb

def van_magasabb(magassag)->bool|str: #vagy logikai vagy string
    for h in hegyek:
        if h.magassag>magassag:
            return h.nev
    return False

def magasabb_mint_db(magassag)->int:
    db=0
    for h in hegyek:
        if h.magassag_lab>magassag:
            db+=1
    return db

def hegy_statisztika()->dict[str,int]:
    stat:dict[str,int]={}
    for h in hegyek:
        if h.hegyseg in stat.keys():
            stat[h.hegyseg]+=1
        else:
            stat[h.hegyseg]=1
    return stat

def mentes(hegyseg,fajlnev):
    f=open(fajlnev,'w',encoding='utf8')
    f.write('Hegycsúcs;Magasság lábban\n')
    for h in hegyek:
        if h.hegyseg==hegyseg:
            f.write(f'{h.nev};{str(round(h.magassag_lab,1)).replace(".",",")}\n')
    f.close()

            