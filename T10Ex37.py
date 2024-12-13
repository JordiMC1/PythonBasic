import random

def crear_num_aleatoris():
    l=[]
    for i in range(4):
        l.append(random.randint(0,9))
    return l
def comparar(l):
    s=[]
    r=[0, 0, 0, 0]
    for i in range(4):
        s.append(int(input("Num: ")))
        if l[i]==s[i]:
            r[i]=2
    for i,e in enumerate(s):
        if e in l and r[i]!=2:
            r[i]=1
    for e in s:
        if e==0:
            print("Aquest número {} no hi és: ".format(e))
        elif e==1:
            print("Aquest número {} existeix però no està al seu lloc".format(s))
        else:
            print("Aquest número {} està en el seu lloc".format(e))

m = crear_num_aleatoris()
comparar(m)