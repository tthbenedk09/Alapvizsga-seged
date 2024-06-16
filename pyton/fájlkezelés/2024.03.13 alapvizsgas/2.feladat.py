from random import randint

def halmaze(lista:list)->str:
    if len(set(lista))==len(lista):
        return 'Halmaznak tekinthető!'
    return 'Halmaznak nem tekinthető!'


print('2. feladat: Halmaz-e?')
for i in range(1,9): # 8 lista kell
    lista:list[int]=[]
    for j in range(5): # 5 elemet generálunk egy listába
        lista.append(randint(0,9))
    print(f'{i}. {lista} -> {halmaze(lista)}')
    