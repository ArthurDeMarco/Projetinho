def fatorial(numero):
    if numero == 0:
        return 1
    fat = 1 
    for i in range(numero, 0, -1):
        fat *= i
    return fat
    
numero =  int(input("Digite o numero que deseja calcular a fatorial: "))
fat = fatorial(numero)
print(f"O fatorial de {numero} é {fat}")