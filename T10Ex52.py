def llegir_llista():
    l = []
    a = "a"
    while a!= ".":
        a = input("Introdueix una paraula: ")
        if a!= ".":
            l.append(a)
    return l

def index_paraula(l, paraula):
    if paraula not in l:
        return -1
    else:
        for i,e in l:
            enumerate(l)
            if e == paraula:
                return i
l = llegir_llista()
p = input("Di quina paraula de la llista vols cercar: ")
n = index_paraula(l, p)
if n>0:
    print("La paraula {} esta en la posició {}.".format(p, n))
else:
    print("La paraula no está dins la llista.")