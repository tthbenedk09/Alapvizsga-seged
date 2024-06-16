def magahangzók_szama(nap):
    darab=0
    magahangzók='aáeéiíoóöőuúüű'
    # hétfő
    for n in nap:
        if n in magahangzók:
            darab+=1
    return darab

napok:list[str]=['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek']

legtobb=napok[0]
for nap in napok[1:]:
    if magahangzók_szama(nap)>magahangzók_szama(legtobb):
        legtobb=nap

print(f'A legtöbb magánhangzó a {legtobb}-ben van.')