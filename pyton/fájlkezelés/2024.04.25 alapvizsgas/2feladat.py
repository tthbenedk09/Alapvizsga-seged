def maganhangzok_szama(nap):
    darab=0
    maganhangzok='aáeéiíoóöőuúüű'
    #hétfő
    for n in nap:
        if n in maganhangzok:
            darab+=1
    return darab

napok:list[str]=['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek']

legtobb=napok[0]
for nap in napok[1:]:
    if maganhangzok_szama(nap)>maganhangzok_szama(legtobb):
        legtobb=nap
print(f'A legtöbb magánhangzó a {legtobb}-ben van.')