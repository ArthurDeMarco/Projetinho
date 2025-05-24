soma = 0

with open("numeros.txt", "r") as arquivo:

    for linha in arquivo.readlines():

        soma += int(linha)

print(soma)