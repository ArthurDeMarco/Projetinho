num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
op = int(input("Selecione o tipo de operacao: Div = 1 Mult = 2 Soma = 3 Sub = 4: "))


if op == 1:
    divisao = num1 / num2
    print("O resultado da operacao e", divisao)
elif op == 2:
    multiplicacao = num1 * num2
    print("O resultado da operacao e", multiplicacao)
elif op == 3:
    soma = num1 + num2
    print("O resultado da operacao e", soma)
elif op == 4:
    subtracao = num1 - num2
    print("O resultado da operacao e", subtracao)
else:   
    print("Valor invalido")
    
    

