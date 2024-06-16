from functions import *

fajlBeolvas('helsinki.txt')

print(f'3. feladat\nPontszerző helyezések száma: {len(eredmenyek)}')

print('4. feladat: ')
print(f'Arany: {helyezesekSzama(1)}')
print(f'Ezüst: {helyezesekSzama(2)}')
print(f'Bronz: {helyezesekSzama(3)}')
print(f'Összesen: {helyezesekSzama(1)+helyezesekSzama(2)+helyezesekSzama(3)}')

print(f'5. feladat:\nOlimpiai pontok száma: {osszPont()}')

print('6. feladat:')
torna=sportagErmek('torna')
uszas=sportagErmek('uszas')
if uszas>torna:
    print('Úszás sportágban szereztek több érmet.')
elif uszas<torna:
    print('Torna sportágban szereztek több érmet.')
else:
    print('Egyenlő volt az érmek száma.')

fajlbaIras('helsinki2.txt')  

legtobb=maxLetszam()
print('8. feladat:')
print(f'Helyezés: {legtobb.helyezes}')
print(f'Sportág: {legtobb.sportag}')
print(f'Versenyszám: {legtobb.versenyszam}')
print(f'Sportolók száma: {legtobb.letszam}')
