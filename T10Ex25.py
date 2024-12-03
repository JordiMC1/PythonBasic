def llegir_llista():
    l=[]
    a=""
    while a!=".":
        a=input("Introdueix un número, per a acabar posa un '.': ")
        if a!=".":
            l.append(int(a))
    return l
def gran_llista(l):
    return max(l)

a = llegir_llista()
print("El nombre més gran de la llista {} és {}".format(a,gran_llista(a)))