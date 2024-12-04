def crear_repetits(n,c):
    return c*n

a= input("Introdueixi un caràcter: ")
b= int(input("Introdueixi el número de vegades que vol repetir el caràcter anterior: "))
print("El caràcter {} repetit {}-vegades és {}".format(a,b,crear_repetits(b,a)))