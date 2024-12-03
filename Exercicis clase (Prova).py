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

#Operacions matemàtiques:
a = 7.0
b = 10.0
c = a + b
print(c)
#Suma: + | Resta: - | Divisió entera: / | Multiplicació: * | Potència: ** | Divisió redondejada: // | etc..

#Comparació:
a = 3
b = "3"
if a == b:
    print("Si es igual")
else:
    print("No es igual")
e = 3 + 4 * 5 / 7 ** (4-27)
print(e)
a = int(input("Escriu un número: "))
b = int(input("Escriu un número: "))
c = int(input("Escriu un número: "))
if a > b:
    if b > c:
        print("{} és major que ")