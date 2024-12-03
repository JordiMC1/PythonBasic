'''a = "Hola"
b = input ("Llegir paraula: ")
# 1. Mostrar caràcter a caràcter la cadena llegida
for e in b:
    print(e)

# 2. Longitut paraula llegida
print (len (b))

# 3. Comparar si les dues paraules son iguals
if a==b:
    print("{} i {} són iguals.".format(a, b))
else:
    print("{} i {} són diferents.".format(a, b))

# 4. Juntar a i b per un guió
print (a+" "+b)

# 5. Repetir 3 vegadas la paraula de b
print (b * 3)

# 6. Cercar si la paraula de a està dins b (string)
if "a" in b:
    print("a és dins l'string {}.".format(b))
else:
    print("a no hi és.")

lb = [1, "Hola", 'b', (1,2), (3,4)]

print (lb[4])

print (lb[0:4:2])

print (lb[4-2])

lb.append([100, 200])
print (lb)

lb.extend([300, 400])
print (lb)

lc = [1, 2, 3, 4]
print (lc)

ld = lb + lc
print (ld)

lp = lc*3
print (lp)

if 1 in lc:
    print("1 és a la llista. ")
else:
    print("1 no és a la llista. ")

lc [1] = 2
lc [3] = 1
print (lc)

del lc [3]
print (lc)

del lc [0:2]
print (lc)

lc.remove (3)
print (lc)

print(len(lc))
print(len(lp))

lp[0] = "1"
print(lp.count(1))

lp[0] = "1"
print (lp.count(1))

lp.pop(0)

lp.reverse()
print(lp)

lpb = lp[::-1]
print(lpb)

print(lpb)

print(lp)
'''
'''p = []
a = "1"
while a != ".":
    a = (input("Introdueix un número(Si vol acabar la llista possi un punt): "))
    if a !=".":
        p.append(int(a))
    else:
        print("Adéu!!")

lp = len (p)
suma = 0
for e in range(lp):
    suma = suma + p(e)

print("La llista {} te una longitud de {} números i la suma de tots els números és {}. ".format(p, lp))

#Repeticions:
l = []
for i in range (4):
        l.append(int(input("Introdueix un número: ")))
print(l)
suma = 0
for e in l:
        suma = suma + e
print("La suma de tota la llista {} és {}".format(l, suma))
'''
'''def ln ():
    l = []
    a = "1"
    while a != ".":
        a = (input("Introdueix un número(Si vol acabar la llista possi un punt): "))
        if a != ".":
            l.append(int(a))
        else:
            print("Adéu!!")
    return l

def sll(misc):
    suma = 0
    for e in misc:
        suma = suma + e
    return suma

#Programa principal
p = ln()
print(p)
suma = sll(p)
print(suma)
print(p[::-1])
print(p)
'''
'''def lll ():
    l = []
    a = "1"
    while a!= ".":
        a = (input("Introdueix un caràcter que no sigui .: "))
        if a!= ".":
            l.append(int(a))
        else:
            print("Adéu!!")
    return l

def ell(l):
    d = dict
    c="qwertyuiopñlkjhgfdsazxcvbnmQWERTYUIOPÑLKJHGFDSAZXCVBNM"
    for e in c:
        d(e) == 0
    return d

def llegir_llista():
    l = []
    a = "1"
    while a!=".":
        a = input("Introdueix una paraula: ")
        if a!=".":
            l.append(a)
        else:
            print("Adéu!!")
    return l

#Programa principal
l = llegir_llista()
cl = set(l)
if len(l) == len(cl):
    print("No hi ha repetides")
else:
    print("Hi ha repetides")
'''
'''a = (1,2,(1,2),3,4)
print(a.count)
print(a.index(2))
for e in a:
    print(a)
b = len(a)
print(b)
a = {"Nom": "Joan","Cognom": "Ramis","Telefon":971360133}
for e in a:
    print("{}: {}".format(e,a[e]))
for x,y in a.items():
    print(x,y)'''
'''a = {"E1":"r1","E2":"V2","E3":{"E31":"Pep","E32":"Ramis"}}
print(a.get("E3"))'''
'''
#Operacions matemàtiques:
a = 7.0
b = 10.0
c = a + b
print(c)
#Suma: + | Resta: - | Divisió entera: / | Multiplicació: * | Potència: ** | Divisió redondejada: // | etc..
'''
'''
#Parametres
#String/cadena de caracters ?? Es passa per valor o per referència
def modifica_string(s):
    s="Aixo es un canvi, anem a veure si fora de la funció queda el canvi o no."

s ="Bon dia, això es una prova"
print(s)
modifica_string(s)
print(s)
#
def operacio (a, b, c,):
    c= a + b
a = 3
b = 4
c = 0
print(c)
operacio(a, b, c)
print(c)

# Per referencia, si modifica el valor
def axllista(l):
    for i in range(len(l)):
        l[i]*=3

llista = [2, 3, 4]
print(llista)
axllista(llista)
print(llista)

def sumarl(llista):
    ls = []
    for e in llista:
        ls.append(e)
    return ls

# Programa principal:
l = [2, 3, 4]
print(l)
s = sumarl(llista)
print("La llista original és {} i la modificada és {}".format(l, s))

l = [1,2,3,4,5]
r = list(map(lambda x:x**2,l))
print(r)
'''
'''
#Llegir si una paraula es més o menys llarga que l'altra
a = input("Posa la primera paraula: ")
b = input("Posa la segona paraula: ")

if len(a) > len(b):
    print("La paraula {} es més llarga que {}.".format(a,b))
else:
    print("La paraula {} és més llarga que {}.".format(b,a))
if len(a)==len(b):
    print("Les dues paraules son igual de llargues.")
'''
'''
#Llegir els nombres parells d'una llista
l = [3,5,6,8,9,11,12]

r = []
for e in l:
    if e%2==0:
        r.append(e)
print(r)

#Versió iterativa
def parell(x):
    if x%2==0:
        r.append(e)
print(r)

#Vesrsió amb filter(programació funcional)
def parell(x):
    if x%2==0:
        return True
    return False
w = list(filter(lambda x:x%2==0,l))
print(w)

#Versió amb funció anònima
s = list(filter(lambda x:x%2==0,l))
print(s)

#Fer el factorial de forma iterativa
n = int(input("Introdueix un número: "))
i = 0
while (i<=n):
    r=r*n
    n=n-1
print(r)

#Fer el factorial en recursivitat
n = int(input("Dime un numero: "))
def fact(n):
    if n <= 0:
        return 1
    else:
        return n*fact(n-1)
print(fact(3))
'''
#Llegir una cadena de caracters i substituir les vocals per un '.' i mostrar el resultat.
def llegir_llista():
    l=[]
    a=""
    while a!=".":
        a=input("Introdueix un caracter, per a acabar posa un '.': ")
        if a!=".":
            l.append((a))
    return l