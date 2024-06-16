from functions import *

print('3. feladat: Toto\n3.1 feladat: Adatok beolvasása és tárolása')
beolvas('toto.txt')

print(f'3.2 feladat: Fogadási fordulók száma: {fordulokSzama()}')

print(f'3.3 feladat: Telitalálatos szelvények száma: {telitalalatosokSzama()} darab')

if dontetlenMentes():
    print('3.4 feladat: Volt döntetlen mentes forduló!')
else:
    print('3.4 feladat: Nem volt döntetlen mentes forduló!')
