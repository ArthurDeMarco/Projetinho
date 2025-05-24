def media(*numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma / len(numeros)
 
resultado = media(3, 5, 9, 4, 11)
print(f"O valor da média é {resultado}")