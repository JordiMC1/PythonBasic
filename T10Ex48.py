def llegir_llista():
    l = []
    a = "a"
    while a!= ".":
        a = input("Introdueix un número: ")
        if a!= ".":
            l.append(int(a))
    return l

def hi_ha_duplicats(l):
    s = set(l)
    if len(l) == len(s):
        print("No hi ha duplicats.")
    else:
        print("Hi ha duplicats")

l = llegir_llista
hi_ha_duplicats(l) 