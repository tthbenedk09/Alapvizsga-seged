from dijazott import dijazott

dijazottak:list[dijazott]=[]

def beolvas(fajlnev):
    f=open(fajlnev,'r',encoding="utf8")
    f.readline() #az első sor címsor, azt kihagyjuk
    for sor in f:
        dijazottak.append(dijazott(sor.strip()))
    f.close()

def tipus_nev_alapjan(nev:str)->str:
    for d in dijazottak:
        if d.teljesnev.upper()==nev.upper():
            return d.tipus
    return "Nincs ilyen díjazott!!!"

def dijazott_ev_es_tipus_alapjan(ev:int,tipus:str)->dijazott|bool:
    for d in dijazottak:
        if d.ev==ev and d.tipus==tipus:
            return d
    return False

def szervezetek_adott_ev_utan(ev:int,tipus:str):
    for d in dijazottak:
        if d.ev>=ev and d.tipus==tipus and d.vezeteknev=="":
            print(f'\t{d.ev}: {d.keresztnev}')

def dijazott_nev_tartalmazza(nev:str):
    for d in dijazottak:
        if nev.upper() in d.vezeteknev.upper(): # ha a keresett részlet benne van a névben
            print(f'\t{d.ev}: {d.teljesnev}({d.tipus})')

def tipus_szerinti_fajlbairas(tipus:str):
    dijazottak2=dijazottak.copy() # lista megfordítása
    dijazottak2.reverse()
    f=open(tipus+'.txt','w',encoding='utf8')
    f.write('Év:Díjazott\n') # ha kell címsor
    for d in dijazottak2:
        if d.tipus==tipus:
            f.write(f'{d.ev}:{d.teljesnev}\n')
    f.close()

def nobeldij_statisztika():
    stat={}
    for d in dijazottak:
        if d.tipus in stat.keys():
            stat[d.tipus]+=1
        else:
            stat[d.tipus]=1
    for key, value in stat.items():
        print(f'\t{str(key).ljust(26)}{value:4d} db')

       #fizikai                   207 db
       #                           79 db 
    

