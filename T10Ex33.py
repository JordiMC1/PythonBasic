def llegir_llista():
    l = []
    a = "a"
    while a!= ".":
        a = input("Intoduiex un nom: ")
        if a!= ".":
            l.append(a)
    return l

def noms_que_comencen_per(l, c):    
    m = []
    for e in l:
        if e[0] == c.upper() or e[0]==c.lower():
            m.append(e)
    print("Els elements de la llista {} que comecen per {} són {}.".format(l,c,m))

l = llegir_llista()
c = input("Introdueix un caracter: ")
noms_que_comencen_per(l, c) 