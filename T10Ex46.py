def llegir_llista():
    l = []
    a = "a"
    while a!= ".":
        a = input("Introdueix un nom: ")
        if a!= ".":
            l.append(a)
    return l


def eiminar_cap_i_cua(l):
    return l[1:-1]

l = llegir_llista()
s = eiminar_cap_i_cua(l)
print("{} es transforma en {}".format(l,s)) 