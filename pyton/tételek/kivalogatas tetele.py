# A feltételeknek megfelelő elemeket beleteszi egy másik listába (másolja)

# 3-mal osztható számok
from random import randint

szamok=[]
for i in range(50):
    szamok.append(randint(-100,100))
print(szamok)

# kiválogatás tétele
harommal_oszthato_szamok=[]
for szam in szamok:
    if szam%3==0:
        harommal_oszthato_szamok.append(szam)
print(f'Hárommal osztható számok: \n{harommal_oszthato_szamok}')