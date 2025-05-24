agenda = {}
while True:
    nome = input("Digite o nome do produto: ")
    valor = input("Digite o valor do produto: ")
    if nome in agenda:
        if input(f"Contato já cadastrado com o número {agenda[nome]}. Deseja alterar? (s/n) ").strip().lower() == "n":
            continue
    agenda[nome] = valor
    if input("Deseja cadastrar um novo produto (s/n): ") == "n":
        break
print(agenda)