def llegir_llista():
    l=[]
    a=""
    while a!=".":
        a=input("Introdueix un número, si vols acabar la llista posa un '.': ")
        if a!=".":
            l.append(int(a))
    return l
def crear_punts(l):
    s="."
    for e in l:
        print("{} \n".format(s*e))
        s="."

a = llegir_llista()
crear_punts(a)