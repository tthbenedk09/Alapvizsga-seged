# Egy lsita bizonyos feltételnek megfelelő elemeit adja össze (összeg, átlag, szorzat) 

from random import randint

szamok=[]

elemszam=randint(10,40)

for i in range(elemszam):
    szamok.append(randint(-100,100))
print(szamok)

#összegzés tétele

# Mennyi a pozitív számok összege?

osszeg=0
for szam in szamok:
    if szam>0:
        osszeg+=1 # osszeg=osszeg+szam
print(f'A pozitív számok összege: {osszeg}')

# Mennyi a páros számok átlaga?

osszeg=0
db=0
for szam in szamok:
    if szam%2==0:
        db+=1
        osszeg+=szam
if db>0:
    print(f'A páros számok átlaga: {osszeg/db}')
else:
    print('Nincs a feltételnek megfeleő elem a listában.')