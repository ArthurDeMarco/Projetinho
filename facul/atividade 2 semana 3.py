menor = 1000000000000;
maior = -100000000000;
for i in range(5):
    num = int(input("Digite o " + str(i + 1) + " numero: "))
    if num < menor:
        menor = num
    elif num > maior:
        maior = num
print("O maior numero e: " , maior, "o menor numero e: " , menor)