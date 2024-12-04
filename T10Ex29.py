def bintodec(b):
    aux = b[::-1]
    d = 0
    for i,e in enumerate(b):
        d+= int (e)* (2**i)    
    return (d)
        
a = input("Introdueix un número en binari: ")
print("El número {} binari és {} decimal.".format(a, bintodec(a)))