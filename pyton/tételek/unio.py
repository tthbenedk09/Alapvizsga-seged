# Unio: a kiinduló listák elemeit összerakjuk egy eredménylistába

from random import randint


szamok1=[]
szamok2=[]


for i in range(50):
    szamok1.append(randint(-100,100))
    szamok2.append(randint(-100,100))
print(f'Számok1:\n{szamok1}')
print(f'Számok2:\n{szamok2}')

# unio

unio=[]
for szam in szamok1:
    unio.append(szam)
for szam in szamok2:
    unio.append(szam)
    
#unio=szamok1+szamok2
print(f'Unio:\n{unio}')