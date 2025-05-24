lista = []

while True:   
    nome = str(input("Digite o seu nome: "))
    rg = int(input("Digite seu Rg: "))
    cpf = int(input("Digite seu cpf: "))
    cadastro = (nome, rg, cpf)
    lista.append(cadastro)
    if input("Deseja cadastrar um novo endereço (s/n): ") == "n":
        break
for i in range(0, len(lista)):
    lest = lista[i]
    print(f"{i}. Nome: {lest[0]}, Rg: {lest[1]}, Cpf: {lest[2]}")