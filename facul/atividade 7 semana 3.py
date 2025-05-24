contador = 0
soma = 0
while True:
    num = int(input("Digite um número (0 para encerrar): "))
    if num == 0:
        break
    else:
        contador += 1
        soma += num
if contador == 0:
    print("Não foram inseridos números a calcular.")
else:
    media = soma / contador
    print("A média dos", contador, "números é", media)

