def menu():
    op = 0
    while op <1 or op>6:
        print ("Tria una opció del menú de la calculadora: ")
        print ("1: Suma")
        print ("2: Resta")
        print ("3: Multiplicació")
        print ("4: Divisió")
        print ("5: Canvis de base")
        print ("6: De tres nombres quin es el més gran")
        print ("7: Sortir")
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
    a = int(input("Posa el nombre de la base a la que vols pasar el teu nombre decimal: 1: Binari   2: Octal    3: Hexadecimal:  "))
    if a==1:
        numero = int(input("Introdueix un nombre decimal per pasar a binari: "))
        print("El teu numero pasat a binari es {}".format(bin(numero)))
    elif a==2:
        numero = int(input("Introdueix un nombre decimal per pasa a octal: "))
        print("El teu numero pasat a binari es {}".format(oct(numero)))
    elif a==3:
        numero = int(input("Introdueix un nombre decimal per pasa a octal: "))
        print("El teu numero pasat a binari es {}".format(hex(numero)))
    elif a>3:
        print("Base equivocada.")

def gran():
    a = int(input("Introdueix el primer nombre: "))
    b = int(input("Introdueix el segon nombre: "))
    c = int(input("Introdueix el tercer nombre: "))
    
    if a>b and c:
        print("El nombre {} és més gros que {} i {}.".format(a,b,c))
    elif b>c and a:
        print("El nombre {} és més gros que {} i {}.".format(b,c,a))
    elif c>a and b:
        print("El nombre {} és més gros que {} i {}.".format(c,a,b))

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
            gran()
        case 7:
            a = False
            print("Adeu, gràcies per haver utilitzat la calculadora! \n")
        case _:
            print("Opció no vàlida \n")