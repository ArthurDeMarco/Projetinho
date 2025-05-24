numeros = []

for i in range (5):
    num = int(input("Digite 5 numeros quais quer: "))
    numeros.append(num)
    
with open("numeros.txt", "w") as arquivos:
    for numero in numeros:
        arquivos.write(str(numero) + "\n")