nota1=float(input("Informa a sua primeira nota: "))
nota2=float(input("Informa a sua segunda nota: "))

media = (nota1+nota2)/2
print(f"Média: {media}")

if media == 10:
    print("Aprovado com distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")