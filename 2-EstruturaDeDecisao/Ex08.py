prod1=float(input("Informa o preço do primeiro produto: "))
prod2=float(input("Informa o preço do segundo produto: "))
prod3=float(input("Informa o preço do terceiro produto: "))

if prod1<prod2 and prod1<prod3:
    print(f"O produto a ser comprado é o primeiro, no valor de {prod1}")
elif prod2<prod1 and prod2<prod3:
    print(f"O produto a ser comprado é o segundo, no valor de {prod2}")
else:
    print(f"O produto a ser comprado é o terceiro, no valor de {prod3}")