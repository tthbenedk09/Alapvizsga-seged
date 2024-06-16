from functions import *

beolvas('Eredmenyek.txt')

print(f'2. feladat: A versenyt {versenyzok_szama()} versenyző fejezte be.')

print(f'3. feladat: Versenyzők száma az "elit junior" kategóriában: {kategoria_letszam("elit junior")} fő')
print(f'3. feladat: Versenyzők száma az "elit" kategóriában: {kategoria_letszam("elit")} fő')

#print(f'4. feladat: Átlagéletkor: {str(round(atlag_eletkor(2014),1)).replace(".",",")} év.')
print(f'4. feladat: Átlagéletkor: {atlag_eletkor(2014):.1f} év.')

bekert_kategoria=input('5. feladat: Kérek egy kategóriát: ')
if len(kategoria_rajtszamok(bekert_kategoria))==0:
    print('\tRajtszám(ok): Nincs ilyen kategória!',end='')
else:
    print('\tRajtszámok: ',end='')
    for rajtszam in kategoria_rajtszamok(bekert_kategoria):
        print(rajtszam,end=' ')

print(f'\n6. feladat: A legjobb időt {gyoztes("n").nev} érte el.')
#print(f'6. feladat: A legjobb időt {gyoztes("f").nev} érte el.')
