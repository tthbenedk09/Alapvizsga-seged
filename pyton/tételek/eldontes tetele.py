# Döntsük el ,hogy van-e valamilyen feltételnek megfelelő elem a listában%!
# Válasz: igen vagy nem (true/false)
# A keresést ne folytassa ha a választ meg tudja adni!

# Van-e 13-mal osztható szám a listában?

szamok=[11,26,33,12,3]
print(szamok)

# v1:
# Hivatalos algoritmus (minden programozási nyelven megvalósítható)
index=0
while index<len(szamok) and szamok[index]%13!=0:
    index+=1
if index==len(szamok):
    print('Nincs 13-mal osztható szám a listában.')
else:
    print('Van 13-mal osztható szám a listában.')

    #v2:
    # Pyton specifikus megoldás
    for szam in szamok:
        if szam%13==0:
            print('Van 13-mal osztható szám a listában.')
            break # az első teljesüléskor kiugrik ciklusból
    else: #csak akkor léo bele ha a for-ban nem volt break
        print('Nincs 13-mal osztható szám a listában.')

#v3
# később saját függvénnyel
