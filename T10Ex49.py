import random

def llista_20_elements():
    print("Els numeros aleatoris del 1 al 100 són: ")
    l = []
    for i in range(20):
        l.append(random.randint(0,101))
    print(l)

llista_20_elements()