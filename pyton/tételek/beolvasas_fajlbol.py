fajl=open('gyumolcsok.txt','r',encoding='UTF8') # 'gyumolcsok.txt' - fájl amit szeretnék beolvasni
# 'r' - megnyitás módja - r: olvasásra
# encoding='UTF8' - karakterkódolás

egysor=fajl.readline() # beolvas 1 sort a fájlból és a mutatót a következő sorra állítja
egysor=egysor.strip() # strip - levágja a sor elejéről és végéről a láthatatlan karaktereket (pl. soremelés)

kovetkezosor=fajl.readline().strip() # itt egyszerre beolvassuk és levágjuka végéről a soremelés karaktert
fajl.close() # fájl bezárása - nagyon fontos!! (főleg írásnál)

print(egysor)
print('teszt')
print(kovetkezosor)
print('---------------------------------------------------------------------------------')

# teljes szövegese fájl beolvasása:
gyumolcsok=[] # lista a fájból érkező adatoknak 
fajl=open('gyumolcsok.txt','r',encoding='UTF8')

for sor in fajl: # végigmegy a fájl a sorain
    gyumolcsok.append(sor.strip())
fajl.close()

print(gyumolcsok)
print('---------------------------------------------------------------------------------')
gyumolcsok.clear() # kiürítjük a listát hogy a következő feladatban is használni tudjuk
# Ha fejléc is van a fájlban
fajl=open('gyumolcsok_fejleccel.txt','r',encoding='UTF8')
fajl.readline() # ha nincs rá szükségünk késöbb
# elso_sor=fajl.readline()

for sor in fajl: # végigmegy a fájl a sorain
    gyumolcsok.append(sor.strip())
fajl.close()

print(gyumolcsok)
