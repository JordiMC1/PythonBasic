def llegir_llista():
    l = []
    a = "a"
    while a!= ".":
        a = input("Introdueix un número: ")
        if a!= ".":
            l.append(int(a))
    return l

def elimina_duplicats(l):
    s = set(l)
    return list(s)
l=llegir_llista
r=elimina_duplicats
print("La llista {} uqeda aixi {}.".format(l,r))

elimina_duplicats(l) 