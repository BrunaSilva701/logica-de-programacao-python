num1=float(input("Informa o primeiro número: "))
num2=float(input("Informa o segundo número: "))
num3=float(input("Informa o terceiro número: "))

#DECRESCENTE
numeros = sorted([num1, num2, num3], reverse=True)
print(f"A ordem decrescente dos números é: {numeros}")

#CRESCENTE
numeros = sorted([num1, num2, num3])
print(f"A ordem crescente dos números é: {numeros}")