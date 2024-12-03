def menu():
    op = 0
    while op <1 or op>6:
        print ("Tria una opció del menú de la calculadora: ")
        print ("1: Suma")
        print ("2: Resta")
        print ("3: Multiplicació")
        print ("4: Divisió")
        print ("5: Canvis de base")
        print ("6: Sortir")
        op = int(input("Introduéix un opció del menú: "))
        return op

def sumar():
    a = int (input("Introdueix el primer element: "))
    b = int (input("Introdueix el segon element: "))
    c = a + b
    print("El resultat de sumar {} més {} és {}".format(a, b, c))

def restar():
    a = int (input("Introdueix el primer element: "))
    b = int (input("Introdueix el segon element: "))
    c = a - b
    print ("El resultat de restar {} menys {} és {}".format(a, b, c))

def multiplicar():
    a = int (input("Introdueix el primer element: "))
    b = int (input("Introdueix el segon element: "))
    c = a * b
    print("El resultat de mutliplicar {} més {} és {}".format(a, b, c))

def dividir():
    a = int (input("Introdueix el primer element: "))
    b = int (input("Introdueix el segon element: "))
    c = a / b
    print("El resultat de dividir {} entre {} és {}".format(a, b, c))

def base():
    a = int (input("Tria el format del teu nombre: 1: Binari 2: Decimal 3: Octal 4: Hexadecimal: "))
    b = int (input("Tria el format del nombre a transformar: 1: Binari 2: Decimal 3: Octal 4: Hexadecimal: "))
    
    c = bin(print("El nombre transformat es: {}") )




a = True
while a:
    op = menu()
    match op:
        case 1:
            sumar()
        case 2:
            restar()
        case 3:
            multiplicar()
        case 4:
            dividir()
        case 5:
            base()
        case 6:
            a = False
            print("Adeu, gràcies per haver utilitzat la calculadora! \n")
        case _:
            print("Opció no vàlida \n")