aux = 0

while True:
    nota = float(input('digite uma nota entre 0 e 10: '))

    if nota >= 0 and nota <= 10:
        break
        print('nota valida. Saindo do programa')
    else:
        print('nota invalida. Digite outra')