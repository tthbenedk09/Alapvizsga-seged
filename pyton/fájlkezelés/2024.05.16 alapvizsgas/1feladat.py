penznem=input('Eurót (EUR) vagy forintot (HUF) akarsz váltani? ')

if penznem=="EUR":
    mennyiseg=int(input('Hány eurót akarsz beváltani? '))
    print(f'{mennyiseg} euróért {mennyiseg*365} forintot kapsz.')
else:    
    mennyiseg=int(input('Hány forintot akarsz beváltani? '))
    print(f'{mennyiseg} forintért {mennyiseg/365:.2f} eurót kapsz.')