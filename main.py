etelnev=["húsleves", "paradicsomleves", "gyümölcsleves"]
etelar=[1200, 1100, 2000]

"""
Most annyi lista van, ahány tulajdonsága az adott ételnek
Úgy lenne a jobb. ha csak egy listánk lenne és egy ételnek egyben kezelhetnénk a tulajdonságait.
Létrehizunk egy étel típust - ez az étel éltalános lírását fogja jelentkeni.
A konkrét étel a típus példányosításakor fog létrejönni./jön létre."""
#print("Az első leves ára", etelnev[0], etelar[0])

from Etel import Etel
etelek=[]
#pédányosítás, az új típus alapján létrehozok egy konkrét előfordulást.
etel=Etel("húsleves", 1200, "leves")
etelek.append(etel)
etel=Etel("paradicsomleves", 1100, "leves")
etelek.append(etel)
etel=Etel("pörkölt", 2300, "főétel")
etelek.append(etel)

for i in range(0,len(etelek),1):
    print(f"Az {i}. étel: {etelek[i].nev}, {etelek[i].ar}, {etelek[i].tipus}")

from Szemely import Szemely
szemelyek=[]
szemely=Szemely("Szabó Anna", 1996, "AO63725173836", "nő")
szemelyek.append(szemely)
szemely=Szemely("Réti András", 1954, "EB82708964647", "férfi")
szemelyek.append(szemely)
szemely=Szemely("Kovács Péter", 1983, "AE84827395726", "férfi")
szemelyek.append(szemely)

for i in range(0, len(szemelyek),1):
    print(f"Az {i}. személy: {szemelyek[i].nev}, {szemelyek[i].evsz}, {szemelyek[i].szemsz}, {szemelyek[i].nem}")
    print(f"{szemelyek[i].nev} {szemelyek[i].kor()} éves.")

for i in range(0, len(szemelyek),1):
    if