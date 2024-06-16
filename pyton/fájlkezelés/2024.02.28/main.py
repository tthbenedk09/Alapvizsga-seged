from HegyekMo import *

beolvas('hegyekMo.txt')

#print(f'3. feladat: Hegycsúcsok száma: {len(hegyek)} db')
print(f'3. feladat: Hegycsúcsok száma: {csucsok_szama()} db') # ha mindent külön fgv-ben kell 

#print(f'4. feladat: Hegycsúcsok átlagos magassága: {atlag_magassag()} m')
print(f'4. feladat: Hegycsúcsok átlagos magassága: {str(atlag_magassag()).replace(".",",")} m')

print('5. feladat: A legmagasabb hegycsúcs adatai:')
legmagasabb=legmagasabb_csucs()
print(f'\tNév: {legmagasabb.nev}')
print(f'\tHegység: {legmagasabb.hegyseg}')
print(f'\tMagasság: {legmagasabb.magassag} m')

magassag=int(input('6. feladat: Kérek egy magasságot: '))
if van_magasabb(magassag)==False:
    print(f'\tNincs {magassag} m-nél magasabb hegycsúcs.')
else:
    print(f'\tVan {magassag} m-nél magasabb hegycsúcs például a(z) {van_magasabb(magassag)}.')

print(f'7. feladat: 3000 lábnál magasabb hegycsúcsok száma: {magasabb_mint_db(3000)}')

print('8. feladat: Hegység statisztika')
for key,value in hegy_statisztika().items():
    print(f'\t{key}: {value} db')

print('9. feladat: mentés')
mentes('Bükk-vidék','bukk-videk.txt')
mentes('Mátra','matra.txt')