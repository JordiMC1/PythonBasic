def menu():
    print("1: Suma ")
    print("2: Resta ")
    print("3: Multiplicació ")
    print("4: Divisió ")
    print("5: Sortir ")

def suma():
    a = float(input("Introdueix el primer numero: "))
    b = float(input("Introdueix el segon numero: "))
    print("El resultat de la suma es: ", a + b)

def resta():
    a = float(input("Introdueix el primer numero: "))
    b = float(input("Introdueix el segon numero: "))
    print("El resultat de la resta es: ", a - b)

def multiplicacio():
    a = float(input("Introdueix el primer numero: "))
    b = float(input("Introdueix el segon numero: "))
    print("El resultat de la multiplicacio es: ", a * b)

def divisio():
    a = float(input("Introdueix el primer numero: "))
    b = float(input("Introdueix el segon numero: "))
    print("El resultat de la divisio es: ", a / b)
    
a = True    
while a:    
    op = menu
    match op:
        case 1:
            suma()
        case 2:
            resta()
        case 3:
            multiplicacio()
        case 4:
            divisio()
        case 5:
            print("Adeu i gracies per emprar la calculadora!!")
        case _:
            print("Error")