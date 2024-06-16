from random import randint

def osszpont(szamok:list):
    return sum(szamok)-max(szamok)

szamok:list[int]=[]
for i in range(5):
    szamok.append(randint(1,10))

print(f'{szamok} -> összpontszám: {osszpont(szamok)} pont')