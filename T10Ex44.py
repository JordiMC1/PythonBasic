def suma_digits():
    num = int(input("Posa un numero (Máxim 4 digits): "))
    suma = sum(int(digit) for digit in str(num))
    if suma % 2 == 0:
        print("La suma dels nombres {} són parells.".format(num))
    else:
        print("La suma dels nombres {} son senars.".format(num))

suma_digits()