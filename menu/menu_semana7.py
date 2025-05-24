arquivo_estudantes = 'estudantes.json'
arquivo_professores = 'professores.json'
arquivo_disciplinas = 'disciplinas.json'
arquivo_turmas = 'turmas.json'
arquivo_matriculas = 'matriculas.json'


import os, sys, re, json


def limpar_tela():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
        
def escrever_lista_em_json(lista, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(lista, arquivo)
        
def ler_lista_em_json(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            lista = json.load(arquivo)
            return lista
    except:
        return {}

def incluir_registro(nome_arquivo, entidade):
    while True:     
        limpar_tela()
        registros = ler_lista_em_json(nome_arquivo)
        nome = input(f"Informe o nome do(a) {entidade}: ").strip()
        cpf = input(f"Informe o CPF do(a) {entidade}: ").strip()
        codigo = input(f"Informe o código do(a) {entidade}: ").strip()

        if not codigo.isdigit():
            print("Código inválido. Deve ser numérico.")
        elif not re.match(r"^[A-Za-zÀ-ÿ\s]+$", nome):
            print("Erro: O nome não pode conter números ou caracteres especiais.")
        else:
            registros[(codigo)] = {
                "cpf": cpf,
                "nome": nome
            }
            escrever_lista_em_json(registros, nome_arquivo)
            input(f"\n{entidade.capitalize()} cadastrado com sucesso! Pressione ENTER para continuar...")
            if input("Deseja adicionar outro? (s/n): ").lower() == 'n':
                break

def listar_registros(nome_arquivo, entidade):
    limpar_tela()
    registros = ler_lista_em_json(nome_arquivo)
    if not registros:
        print(f"Não há {entidade}s cadastrados.")
    else:
        print(f"Lista de {entidade}s:")
        for codigo, dados in registros.items():
            print(f"Código - {codigo:<10} | Nome - {dados['nome']:<20} | CPF - {dados['cpf']:<14}")
    input("\nPressione ENTER para continuar...")

def atualizar_registro(nome_arquivo, entidade):
    limpar_tela()
    registros = ler_lista_em_json(nome_arquivo)
    cod = input(f"Informe o código do(a) {entidade} que deseja atualizar: ").strip()
    if cod in registros:
            novo_nome = input("Informe o novo nome: ").strip()
            novo_codigo = input("Informe o novo código: ").strip()
            novo_cpf = input("Informe o novo CPF: ").strip()

            if not novo_codigo.isdigit():
                print("Código inválido. Deve ser numérico.")
            elif not re.match(r"^[A-Za-zÀ-ÿ\s]+$", novo_nome):
                print("Nome inválido. Use apenas letras e espaços.")
            else:
                novo_codigo = int(novo_codigo)
                if novo_codigo != cod:
                    registros[novo_codigo] = registros.pop(cod)
                    cod = novo_codigo
                registros[cod]["nome"] = novo_nome
                registros[cod]["cpf"] = novo_cpf
                escrever_lista_em_json(registros, nome_arquivo)
                print("Dados atualizados com sucesso!")       
    else:
        print("Código inválido. Deve ser um número.")
    input("\nPressione ENTER para continuar...")

def excluir_registro(nome_arquivo, entidade):
    limpar_tela()
    registros = ler_lista_em_json(nome_arquivo)
    cod = input(f"Informe o código do(a) {entidade} a excluir: ").strip()
    if cod in registros:
            registros.pop(cod)
            escrever_lista_em_json(registros, nome_arquivo)
            print(f"{entidade.capitalize()} excluído com sucesso.")
    else:
        print("Código não encontrado.")
    input("\nPressione ENTER para continuar...")
    

while True:
    limpar_tela()
    print("---- MENU PRINCIPAL ----")
    print("(1) Gerenciar Estudantes ")
    print("(2) Gerenciar Professores ")
    print("(3) Gerenciar Disciplinas ")
    print("(4) Gerenciar Turmas ")
    print("(5) Gerenciar Matriculas ")
    print("(9) Sair")
    
    opcao = str(input("Digite o valor respectivo a funcao de sua preferencia: "))

    if opcao == "1":
        while True:
            limpar_tela()
            print("** [ESTUDANTES] MENU DE OPERACOES **")
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Atualizar.")
            print("(4) Excluir.")
            print("(5) Voltar ao menu principal.")

            opcao_aluno = input("Digite a opção: ")

            if opcao_aluno == "1":
                incluir_registro(arquivo_estudantes, "estudante")
            elif opcao_aluno == "2":
                listar_registros(arquivo_estudantes, "estudante")
            elif opcao_aluno == "3":
                atualizar_registro(arquivo_estudantes, "estudante")
            elif opcao_aluno == "4":
                excluir_registro(arquivo_estudantes, "estudante")
            elif opcao_aluno == "5":
                break
            else:
                print("Opção inválida.")
                input("Pressione ENTER...")

    elif opcao == "2":
        print("EM DESENVOLVIMENTO")
        input("\nPressione ENTER para continuar...")

    elif opcao == "3":
        print("Em desenvolvimento")
        input("\nPressione ENTER para continuar...")

    elif opcao == "4":
        print("Em desenvolvimento")
        input("\nPressione ENTER para continuar...")

    elif opcao == "5":
        print("Em desenvolvimento")
        input("\nPressione ENTER para continuar...")

    elif opcao == "9":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
        input("\nPressione ENTER para continuar...")