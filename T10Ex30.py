any_actual = int(input("En quin any esteim?: "))
dades = []
for i in range(4):
    nom = (input("Dime el teu nom: "))
    any_naixement = int(input("Dime el teu any de naixement: "))
    edad = any_actual - any_naixement
    dades.append((nom, any_naixement, edad))

print("Any actual: {}".format(any_actual))
print("Nom\t     \tData naixement         \tAnys que fará aquest any")
for nombre, any_naixement, edad in dades:
    print("{}\t{}             \t{}".format(nom, any_naixement, edad)) 