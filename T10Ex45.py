def digits_parells():
    num = int(input("Posa un numero: "))
    parells = [digit for digit in str(num) if int(digit) % 2 == 0]

    if parells:
        print("Els digits parells de {} son {}".format(num, parells))
    else:
        print("No hi ha nombres parells.")
digits_parells()