def quants_digits_te():
    num = int(input("Posa un número del 1 al 900000: "))
    a = 0
    if num <= 900000 and num >=1:
        digits = len(str(num))
        print("el teu nombre te {} digits de llargaria.".format(digits))
    else: 
        print("El teu numero no está entre l'1 i el 900000.")    
    
quants_digits_te() 