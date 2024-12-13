def mostrar_majors_que(referencia, tupla):        
    for a in tupla:
        if a > referencia:
            print(a)

valors = (input("Intodueix numeros separats per espais: "))

tupla = tuple(map(int, valors.split()))

referencia = 18

a = print("Els nombres majors a {} són: ".format(referencia))

mostrar_majors_que(referencia, tupla)