from functions import *

beolvas('paintings.txt')

print(f'3.3. feladat: A fájlban tárolt festmények száma: {festmenyekSzama()}')

print(f'3.4 feladat: A Pablo Picasso képek száma: {festoFestmenyeinekSzama("Pablo Picasso")} darab.')

legdragabb=legdragabbKep()
print(f'3.5 feladat: A legdrágább kép festője: {legdragabb.festo}, a kép címe: {legdragabb.festmeny}, becsült értéke: {legdragabb.becsultAr} dollár.')

if vanE():
    print('3.6 feladat: Van olyan festmény, amelynek bescsült értéke nem haladja meg az eredeti árát.')
else:
    print('3.6 feladat: Nincs olyan festmény, amelynek bescsült értéke nem haladja meg az eredeti árát.')
