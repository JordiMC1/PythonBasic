def base():
    option = int(input("Vols convertir de (1: binari, 2: octal:, 3: decimal, 4: hexadecimal): "))
    match(option):
        case 1:
            a = int(input("Introdueix el numero: "))
            print("El numero en binari es: ", bin(int(str(a), 2)))
            print("El numero en octal es: ", oct(int(str(a), 2)))
            print("El numero en decimal es: ", int(str(a), 2))
            print("El numero en hexadecimal es: ", hex(int(str(a), 2)))