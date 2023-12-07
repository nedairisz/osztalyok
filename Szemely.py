import datetime

class Szemely:
    def __init__(self, nev:str, evsz:int, szemsz:str, nem:str):
        self.nev=nev
        self.evsz=evsz
        self.szemsz=szemsz
        self.nem=nem


# minden egyes metódusnak paramétere a self
#tagfüggvény, vagy osztál metódus. Az osztály adattagjain végeznek műveleteket

    def kor(self):
        x = datetime.datetime.now()
        return x.year-self.evsz