from functions import *

beolvas('varosok.txt')

print(f'3. feladat: Városok száma: {len(varosok)}')
#print(f'3. feladat: Városok száma: {varosokSzama()}') # ha mindent külön fügvénnyel kell

print(f'4. feladat: indiai nagyvárosok lakosságának összege: {orszagLakossaga("India")} fő')
#print(f'4. feladat: kínai nagyvárosok lakosságának összege: {orszagLakossaga("Kína")} fő')

legnagyobb=legnagyobbVaros()
print('5. feladat: A legnagyobb város adatai:')
print(f'\tNév: {legnagyobb.nev}')
print(f'\tOrszág: {legnagyobb.orszag}')
print(f'\tLakosság: {legnagyobb.lakossag} ezer fő')

if orszagKeres('Magyarország'):
    print('6. feladat: Van magyar város az adatok között.')
else:
    print('6. feladat: Nincs magyar város az adatok között.')

# if orszagKeres('Kína'):
#     print('6. feladat: Van kínai város az adatok között.')
# else:
#     print('6. feladat: Nincs kínai város az adatok között.')
    
print(f'7. feladat: Városok egy szóközzel: {szokozosVarosok(1)} db')
# print(f'7. feladat: Városok két szóközzel: {szokozosVarosok(2)} db')
# print(f'7. feladat: Városok szóköz nélkül: {szokozosVarosok(0)} db')

print('8. feladat: Ország statisztika')
for key,value in orszagStatisztika().items():
    if value>6:
        print(f'\t{key} - {value} db')

print('9. feladat: kina.txt')
orszagMentes('kina.txt','Kína')
# print('9. feladat: usa.txt')
# orszagMentes('usa.txt','USA')


