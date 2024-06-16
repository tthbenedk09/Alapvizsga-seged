from data import FogadasiFordulo

fordulok:list[FogadasiFordulo]=[]

def beolvas(fajlnev:str):
    f=open(fajlnev,'r',encoding='utf8')
    f.readline()
    for sor in f:
        fordulok.append(FogadasiFordulo(sor))
    f.close()

def fordulokSzama()->int:
    return len(fordulok)

def telitalalatosokSzama()->int:
    db=0
    for fordulo in fordulok:
        db+=fordulo.t13p1
    return db

def dontetlenMentes()->bool:
    for fordulo in fordulok:
        if 'X' not in fordulo.eredmenyek:
            return True
    return False