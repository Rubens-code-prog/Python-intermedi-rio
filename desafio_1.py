# Converta o loop abaixo para uma compreensão de lista


valores = [30, 50, 100, 120]

triplos = []
for valor in valores:
    triplo = valor * 3
    triplos.append(triplo)

print(triplos)

triplos_compreendido = [valor * 3 for valor in valores]
print(triplos_compreendido)
