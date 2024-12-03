def llegir_llista():
    l=[]
    a=""
    while a!=".":
        a=input("Introdueix una paraula, per a acabar posa un '.': ")
        if a!=".":
            l.append((a))
    return l
def gran_llista(l):
    return max(l)

a = llegir_llista()
print("La paraula més gran de la llista {} és {}".format(a,gran_llista(a)))