zoldseg=input('Adja meg a zöldség nevét: ')

# fajl=open('zoldsegek.txt','w',encoding='UTF8')
# 'w' - írással nyitja meg a fájlt
# ha nem létezik, létrehozza
# ha létezik, felülírja!!

fajl=open('zoldsegek.txt','a',encoding='UTF8')
# 'a' - append -hozzáfűzésre nyitja meg a fájlt
# ha nem létezik, létrehozza
# ha létezik, felülírja!!

# fajl.write(f'{zoldseg}\n') # 1 sor írása a fájlba
fajl.write(zoldseg+'\n') # 1 sor írása a fájlba
# \n kell hogy soremelést csináljon a fájlban

zoldsegek=['hagyma','zeller','cékla','karfiol','borsó']
# lista tartalmának fájlba írása soronként
for zoldseg in zoldsegek:
    fajl.write(zoldseg+'\n')

fajl.close()