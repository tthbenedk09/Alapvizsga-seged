from functions import *

print('3. feladat: CB-Rádió')
beolvas('cb.txt')

#print(f'3.2 feladat: Bejegyzések száma: {len(cbAdasok)} db') # ha nem kell mindent függvénnyel!!!

print(f'3.2 feladat: Bejegyzések száma: {bejegyzesek_szama()} db') # ha mindent külön függvénnyel kell!!

print(f'3.3 feladat: Sanyihoz tartozó bejegyzések: {nev_bejegyzesSzam("Sanyi")} db')

print(f'3.4 feladat: A legtöbb adás:')
for adas in cbAdasok:
    if adas.darab==maxAdasDb(): # ha megegyezik a maximummal
        print(f'\tIdő: {adas.ora}:{adas.perc} Darab: {adas.darab} Név: {adas.nev}')

fajlbaIras('cb2.txt')        
