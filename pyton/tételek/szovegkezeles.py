mondat="Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsum reiciendis odio reprehenderit fugiat fugit, laborum natus voluptas commodi excepturi in, ipsa autem? Error dolores sapiente reprehenderit exercitationem officia quos cupiditate."

# Milyen hosszú a mondat?
print(f'A mondat {len(mondat)} karakterből áll.')
print(f'A mondat {len(mondat.replace(" ", ""))} karakterből áll szóközök nélkül.')

# Hány szóból áll a mondat? (szóközök száma+1)
# v1
db=0
for betu in mondat:
    if betu==' ':
        db+=1
print(f'A mondat {db+1} szóból áll.')

#v2
szavak=mondat.split(' ') # határolókarakter (szóköz) mentén szétdarabojuk a mondatot és a szavak listába tesszük
print(f'A mondat {len(szavak)} szóból áll.')

# Hány olyan szó van a szövegben ami legalább 10 karakter hosszú.
irasjelek='([{,.?!-_:}])' # nemkívánatos karakterek törlése
for irasjel in irasjelek:
    mondat2=mondat.replace(irasjel,'')

szavak2=mondat2.split(' ')
db=0
for szo in szavak2:
    if len(szo)>=10:
        db+=1
print(f'A szövegben {db} db szó van, amely legalább 10 karakter hosszú')

# Kérjünk be egy karaktert és mondjuk meg hogy mennyi van belőle!
bekert_karakter=input('Karakter: ')
db=0
for betu in mondat:
    if betu==bekert_karakter:
        db+=1
print(f'A szövegben {db} db {bekert_karakter} karakter van.')

# Melyik karakterből mennyi van a mondatban?
# Ne legyen különbség a kicsi és a nagy betűk között (a=A)
lehetseges_karakterek='qwertzuiopőúóüöasdfghjkléáűmnbvcxyí'
karakterek_szama=[]
for lehetseges_karakter in lehetseges_karakterek:
    db=0
    for karakter in mondat:
        if karakter.upper()==lehetseges_karakter.upper():
            db+=1
    karakterek_szama.append(db)
print('Karakter statisztika: ')
for i in range(len(lehetseges_karakterek)):
    if karakterek_szama[i]>0:
        print(f'{lehetseges_karakterek[i]}: {karakterek_szama[i]}')

# Melyik karakterből van a legtöbb a szövegben?
max_index=0
for i in range(1,len(karakterek_szama)):
    if karakterek_szama[i]>karakterek_szama[max_index]:
        max_index=i
print(f'A {lehetseges_karakterek[max_index]}karakterből van a legtöbb a ({karakterek_szama[max_index]}db)')