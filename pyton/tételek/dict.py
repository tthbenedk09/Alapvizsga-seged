szotar={'alma':'apple','szék':'chair','ajtó':'door','kék':'blue'}
# 'alma':'apple' --> kulcs:érték - key:value párok alkotják
# 'szék':'chair'
# 'ajtó':'door'
# 'kék':'blue'

print(szotar) # teljes szótár kiírása
print(szotar['kék']) # a key mező alapján kiírja a value tartalmát

for szo in szotar.keys(): # végigmegyünk a szótár key mezőzin
    print(szo)  # és kiírjuk azokat

for szo in szotar.values(): # végigmegyünk a szótár value mezőzin
    print(szo)  # és kiírjuk azokat

for szo in szotar.items(): # végigmegyünk a szótáron mezőzin
    print(szo)  # és kiírjuk a key-value értéket

# új elem hozzáadása a szótárhoz
szotar['piros']='red' # dict_neve['key_mező]=value_mező

# meglévő elem felülírása
szotar['kék']='navy'


for key,value in szotar.items(): # végigmegyünk a szótáron mezőzin
    print(f'{key} - {value}')  # és kiírjuk a key-value értéket SZÉPEN

# hiba ha olyan kulcsra hivatkouzunk amelyik nem szerepel a szotárban
# print(szotar['barna']) # KeyError

# keresés szótárban key mező alapján
keresett_szo=input('Keresett szó: ')
if keresett_szo in szotar.keys():
    print(f'{keresett_szo} - {szotar[keresett_szo]}') # akkor írjuk a hozzátartozó értéket
else: # ha nincs benne a szótárban
    print(f'A "{keresett_szo}" nincs benne a szótárban!')
    if input('Szeretné felvenni? (i/n): ')=='i': # ha a válasz 'i'
        jelentes=input('Jelentés: ')
        szotar[keresett_szo]=jelentes

print(szotar)