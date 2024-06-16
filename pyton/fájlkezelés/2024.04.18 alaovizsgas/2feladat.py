from random import randint
import math

def ez_prím(szam):
    for i in range(2,int(math.sqrt(szam))+1):
        if szam%i==0:
            return False
    return True

def vanePrim():
    for szam in szamok:
        if ez_prím(szam): # ha True
            return "Van prímszám a listában!"
    return "Nincs prímszám a listában!"
    

szamok=[]
for i in range(10):
    szamok.append(randint(10,99))

print(szamok)
print(vanePrim())