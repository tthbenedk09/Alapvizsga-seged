# megszámolja egy bizonyos feltételnek megfelelő elemek db-számát a listában

from random import randint

szamok=[]

elemszam=randint(10,40)

for i in range(elemszam):
    szamok.append(randint(-100,100))
print(szamok)

# megszámlásás tétele

#  hány db páros szám van a listában
db=0
#for i in range(len(szamok)):
for szam in szamok:
    if szam%2==0: # azaz ha páros a szám
        db+=1
print(f'A listában {db} páros szám van.')

# hány db negatív szám van a listában
db=0
for szam in szamok:
    if szam<0:
        db+=1
print(f'A listában {db} negatív szám van.')
