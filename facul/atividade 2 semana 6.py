def fatorial(numero):
    # segundo as propriedades de fatorial
    if numero == 0:
        return 1
 
    return numero * fatorial(numero - 1)
 
numero = int(input("Digite um número inteiro para calcular seu fatorial: "))
fat = fatorial(numero)
print(f"O fatorial de {numero} é {fat}")