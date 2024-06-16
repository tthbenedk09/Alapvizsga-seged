class Eredmeny:
    def __init__(self,sor:str) -> None:
        adatok=sor.strip().split(' ')
        self.helyezes=int(adatok[0])
        self.letszam=int(adatok[1])
        self.sportag=adatok[2]
        self.versenyszam=adatok[3]
    
    def pont(self)->int:
        match self.helyezes:
            case 1: return 7 
            case 2: return 5
            case 3: return 4
            case 4: return 3
            case 5: return 2
            case 6: return 1

    def pont2(self)->int:
        if self.helyezes==1: 
            return 7
        else:
            return 7-self.helyezes