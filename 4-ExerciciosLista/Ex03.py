#Estruturas de dados - Lista, dicionario, tupla
# len - retorna a quantidade de elementos da lista

#Lista
# nota = [1, 2, 3, 4]
# print(nota[1])
# print(len(nota))

# Adicionar valor
# nota.append(6)

# Retirar valor
# nota.remove(3)

notas = []

for i in range (0,4):
    notas.append(int(input()))
print(f'A média é {sum(notas)/len(notas)}')