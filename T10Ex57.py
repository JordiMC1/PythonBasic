def crear_llista_fitxer(filename):
    l = []
    wordsFile = open(filename, "r")
    for line in wordsFile:
        for word in line.split():
            l.append(word.strip())
    wordsFile.close()
    return l

def elements_parells(l):
    for i in range(0, len(l), 2):
        print([i])

print(elements_parells(crear_llista_fitxer("words.txt")))