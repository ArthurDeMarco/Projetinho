numeros = []
maior = []
menor = []

for i in range(6):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

media = sum(numeros) / 6

for numero in numeros:
    if numero >= media:
        maior.append(numero)
    else:
        menor.append(numero)

print("A media  foi: ", media)
print("A lista com os valores maiores que a media foi", maior)
print("A lista com os valores menores que a media foi", menor)