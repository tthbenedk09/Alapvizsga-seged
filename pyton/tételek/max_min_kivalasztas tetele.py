# a lista legkisebb vagy legnagyobb elemét adja vissza

from random import randint

szamok=[]

elemszam=randint(10,40)

for i in range(elemszam):
    szamok.append(randint(-100,100))
print(szamok)

# maximum-kiválasztás tétele:

# melyik a legnagyobb szám? (mindegy hoghy hol van a listában)
legnagyobb=szamok[0] # tegyük fel hogy ez a legnagyobb ha találunk nála nagyobbat akkor majd átírjuk
#for szam in szamok: # ez 1* fölöslegesen fog lefutni (0. elemethasonlítja a 0. elemhez)
for i in range(1,len(szamok)):
    if szamok[i]>legnagyobb:
        legnagyobb=szamok[i]
print(f'legnagyobb elem: {legnagyobb}')

#hányadik a legnagyobb szám a listában? (ebből azt is tudjuk természetesen hogy mi a legnagyobb)
legnagyobb_indexe=0 # feltételezzük hogy az első elem
for i in range(1,len(szamok)):
    if szamok[i]>szamok[legnagyobb_indexe]:
        legnagyobb_indexe=i
print(f'A legnagyobb szám a(z) {szamok[legnagyobb_indexe]}, sorszáma: {legnagyobb_indexe+1}')

# Hányadik a legnagyobb páratlan szám
#98,43,46,88,75,92,89      li=4
legnagyobb_indexe=len(szamok) #olyan indexet kell kezdőértéknek adni amit biztosan felülírunk!!
for i in range(len(szamok)):
    if szamok[i]%2==1: # ha páratlan
        if legnagyobb_indexe==len(szamok) or szamok[i]>szamok[legnagyobb_indexe]:
            legnagyobb_indexe=i
print(f'A legnagyobb páraltan szám: {szamok[legnagyobb_indexe]}')