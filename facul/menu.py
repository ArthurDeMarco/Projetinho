estudantes = {}
professores = {}
disciplinas = {}
turmas = {}
matriculas = {}


import os, sys, re

def limpar_tela():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def incluir_registro(registro_dict, entidade):
    while True:
        limpar_tela()
        nome = input(f"Informe o nome do(a) {entidade}: ").strip()
        cpf = input(f"Informe o CPF do(a) {entidade}: ").strip()
        codigo = input(f"Informe o código do(a) {entidade}: ").strip()

        if not codigo.isdigit():
            print("Código inválido. Deve ser numérico.")
        elif not re.match(r"^[A-Za-zÀ-ÿ\s]+$", nome):
            print("Erro: O nome não pode conter números ou caracteres especiais.")
        else:
            registro_dict[int(codigo)] = {
                "cpf": cpf,
                "nome": nome
            }
            input(f"\n{entidade.capitalize()} cadastrado com sucesso! Pressione ENTER para continuar...")
            if input("Deseja adicionar outro? (s/n): ").lower() == 'n':
                break

def listar_registros(registro_dict, entidade):
    limpar_tela()
    if not registro_dict:
        print(f"Não há {entidade}s cadastrados.")
    else:
        print(f"Lista de {entidade}s:")
        for codigo, dados in registro_dict.items():
            print(f"Código - {codigo:<10} | Nome - {dados['nome']:<20} | CPF - {dados['cpf']:<14}")
    input("\nPressione ENTER para continuar...")

def atualizar_registro(registro_dict, entidade):
    limpar_tela()
    cod = input(f"Informe o código do(a) {entidade} que deseja atualizar: ").strip()
    if cod.isdigit():
        cod = int(cod)
        if cod in registro_dict:
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
                    registro_dict[novo_codigo] = registro_dict.pop(cod)
                    cod = novo_codigo
                registro_dict[cod]["nome"] = novo_nome
                registro_dict[cod]["cpf"] = novo_cpf
                print("Dados atualizados com sucesso!")
        else:
            print("Código não encontrado.")
    else:
        print("Código inválido. Deve ser um número.")
    input("\nPressione ENTER para continuar...")

def excluir_registro(registro_dict, entidade):
    limpar_tela()
    cod = input(f"Informe o código do(a) {entidade} a excluir: ").strip()
    if cod.isdigit():
        cod = int(cod)
        if cod in registro_dict:
            registro_dict.pop(cod)
            print(f"{entidade.capitalize()} excluído com sucesso.")
        else:
            print("Código não encontrado.")
    else:
        print("Código inválido. Deve ser um número.")
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
                incluir_registro(estudantes, "estudante")
            elif opcao_aluno == "2":
                listar_registros(estudantes, "estudante")
            elif opcao_aluno == "3":
                atualizar_registro(estudantes, "estudante")
            elif opcao_aluno == "4":
                excluir_registro(estudantes, "estudante")
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