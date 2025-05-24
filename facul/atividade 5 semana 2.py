print("Responda a pergunta com as letras representando M manhã, T tarde ou N noite")
periodo = input("Em que periodo do dia voce trabalha?")

if periodo == "M":
    print("Voce trabalha pela manha")
elif periodo == "T":
    print("Voce trabalha pela tarde")
elif periodo == "N":
    print("Voce trabalha pela noite")
else:   
    print("Valor invalido")