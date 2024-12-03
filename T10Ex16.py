def llegir_llista():
    l=[]
    a=""
    while a!=".":
        a = input("Intro un número de la llista, per acabar la llista posi '.': ")
        if a!=".":
            l.append(int(a))
    return l
def longitud(l):
    i=0
    for e in l:
        i +=1
    return i

x = llegir_llista()
print("La longitud de la llista és: ")
print(longitud(x))