def incluir():
    nome = input("Insira o nome o qual deseja incluir na lista: ")
    telefone = input("Informe o telefone do nome citado")
    clientes[nome] = {"telefone": telefone}
    input("\n Nome adicionado com sucesso pressione enter para continuar...")
    return nome, telefone

def remover():
    nome_remover = input("Informe o nome que deseja remover da lista: ")
    if nome_remover in clientes:
        clientes.pop(nome_remover)
        print("\n Contado excluido com sucesso")
        return True
    else:
        print("O nome informado não se encontra!!")
        return False 
 
def menu():
    print("---- MENU PRINCIPAL ----")
    print("(1) Inserir ")
    print("(2) Remover ")
    print("(3) Sair ")

    opcao = int(input("Escolha qual opção deseja utilzar clicando seu respectivo numero: "))
    return opcao 

clientes = {}
while True:
    op = menu()
    if op == 1:
        incluir()
    elif op == 2:
        remover()
    else:
        input("\n Terminando operacao...")
        break
