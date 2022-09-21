lista_zakupow = {'warzywniak': ('koperek', 'cebula', 'ziemniaki'), 'miesny': ('wedlina', 'schab')}


for a, b in lista_zakupow.items():
    print("W sklepie", a,"kupuje", b)

print("W sumie kupuje", len(lista_zakupow.values()), "produktów")