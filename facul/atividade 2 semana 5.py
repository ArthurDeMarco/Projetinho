lista = []

while True:   
    nome = str(input("Digite o seu nome: "))
    matricula = int(input("Digite sua matricula: "))
    dependentes = tuple()
    while True:
            dependente = input("Digite seu dependente, digite 0 caso queria sair: ")
            if dependente == "0":
                break
            else:
                dependentes += (dependente,)
    cadastro = (nome, matricula, dependentes)
    lista.append(cadastro)
    if input("Deseja cadastrar um novo endereço (s/n): ") == "n":
        break
for i in range(0, len(lista)):
    lest = lista[i]
    print(f"{i}. Nome: {lest[0]}, Matricula: {lest[1]}, Dependente: {lest[2]}")