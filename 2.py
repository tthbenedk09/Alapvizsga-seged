# Monsjuk meg hogy egy elem benne van-e a listában és ha igen akkor hányadik?

from random import randint
szamok=[]
for i in range(20):
    szamok.append(randint(-100,100))
print(szamok)

keresett=int(input('Keresett szám: '))

#v1
# Univerzális megoldás
index=0
while index<len(szamok) and szamok[index]!=keresett:
    index+=1
    # Az első megtalált elem indexét adja vissza utána kilép
if index==len(szamok):
    print('A keresett szám nincs benne a listában.')
else:
    print(f'A keresett szám a {index+1}.a listában.')

#v2:
# Pyton specifikus megoldás
for i in range(len(szamok)):
    if szamok[i]==keresett:
        print(f'A keresett szám a {i+1}.a listában.')
        break
else:
    print('A keresett szám nincs benne a listában.')