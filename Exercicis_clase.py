s = input ("Introdueix la cadena de carácters: ")
l = list(s)
r = []
for e in l:
    if e in "QWERTYUIOPASDFGHJKLÑZXCVBNM":
        r.append(".")
    else:
        r.append(e)
s =  " ".join(r)
print(s)