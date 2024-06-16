from data import Varos

varosok:list[Varos]=[]

def beolvas(fajlnev:str):
    f=open(fajlnev,'r',encoding='utf8')
    f.readline()
    for sor in f:
        varosok.append(Varos(sor))
    f.close()

def varosokSzama()->int:
    return len(varosok)

def orszagLakossaga(orszag:str)->int:
    osszeg=0
    for v in varosok:
        if v.orszag==orszag:
            osszeg+=v.lakossag
    return osszeg*1000 # mert itt nem 1000 főben kérik, hanem simán főben     

def legnagyobbVaros()->Varos:
    legnagyobb=varosok[0]       
    for v in varosok[1:]:
        if v.lakossag>legnagyobb.lakossag:
            legnagyobb=v
    return legnagyobb

def orszagKeres(orszag:str)->bool:
    for v in varosok:
        if v.orszag==orszag:
            return True
    return False

def szokozosVarosok(szokozokSzama:int)->int:
    darab=0
    for v in varosok:
        if v.szokozokDb()==szokozokSzama:
            darab+=1
    return darab # a paraméterként kapott szóközt tartalmazó városok száma

def orszagStatisztika()->dict[str,int]:
    stat:dict[str,int]={}
    for v in varosok:
        if v.orszag in stat.keys():
            stat[v.orszag]+=1
        else:
            stat[v.orszag]=1
    return stat

def orszagMentes(fajlnev:str, orszag:str):
    f=open(fajlnev,'w',encoding='utf8')
    for v in varosok:
        if v.orszag==orszag:
            f.write(f'{v.nev};{v.lakossag}\n')
    f.close()