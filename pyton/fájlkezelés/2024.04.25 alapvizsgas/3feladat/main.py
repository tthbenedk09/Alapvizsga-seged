from functions import *

beolvas('legmagasabb.txt')

print(f'3.2 feladat: Épületek száma: {epuletek_szama()} db')

print(f'3.3 feladat: Emeletek összege: {emeletek_osszege()}')

print('3.4 feladat: A legmagasabb épület adatai')
legmagasabb=legmagasabb_epulet()
print(f'\tNév: {legmagasabb.nev}')
print(f'\tVáros: {legmagasabb.varos}')
print(f'\tOrszág: {legmagasabb.orszag}')
print(f'\tMagasság: {legmagasabb.magassag} m')
print(f'\tEmeletek száma: {legmagasabb.emeletek}')
print(f'\tÉpítés éve: {legmagasabb.epult}')

if van_orszag('Olaszország'):
    print('3.5 feladat: Van olasz épület az adatok között!')
else:
    print('3.5 feladat: Nincs olasz épület az adatok között!')
