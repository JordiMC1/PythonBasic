def noms_que_comencen_per(a, l):
    return [nom for nom in a if nom[0] == l]

print(noms_que_comencen_per(["Joan", "Maria", "Pere", "Anna"], "J")) 