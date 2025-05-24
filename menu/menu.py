"""
Nome: Arthur Andrade De Marco  
Curso: Análise e Desenvolvimento de Sistema  
Descrição: Aqui segue a primeira atividade somativa da semana 8 da matéria de Raciocínio Computacional. 

"""
#Arquivos Json

arquivo_estudantes = 'estudantes.json'
arquivo_professores = 'professores.json'
arquivo_disciplinas = 'disciplinas.json'
arquivo_turmas = 'turmas.json'
arquivo_matriculas = 'matriculas.json'

# Bibliotecas e função para poder limpar a tela no código e o Json

import os, sys, re, json


def limpar_tela():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

#Função para poder escrever os dados em Json
        
def escrever_lista_em_json(lista, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(lista, arquivo)
        
#Função para poder ler os dados em Json

def ler_lista_em_json(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            lista = json.load(arquivo)
            return lista
    except:
        return {}
    
#Função para poder incluir os dados os arquivos

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
        
#Função para poder incluir os dados os arquivos para o tópico de disciplina

def incluir_registro_disciplina(nome_arquivo, entidade):
    while True:     
        limpar_tela()
        registros = ler_lista_em_json(nome_arquivo)
        nome = input(f"Informe o nome do(a) {entidade}: ").strip()
        codigo = input(f"Informe o código do(a) {entidade}: ").strip()

        if not codigo.isdigit():
            print("Código inválido. Deve ser numérico.")
        elif not re.match(r"^[A-Za-zÀ-ÿ\s]+$", nome):
            print("Erro: O nome não pode conter números ou caracteres especiais.")
        else:
            registros[(codigo)] = {
                "nome": nome
            }
            escrever_lista_em_json(registros, nome_arquivo)
            input(f"\n{entidade.capitalize()} cadastrado com sucesso! Pressione ENTER para continuar...")
            if input("Deseja adicionar outro? (s/n): ").lower() == 'n':
                break

#Função para poder incluir os dados os arquivos para o tópico das turmas

def incluir_registro_turmas(nome_arquivo, entidade):
    while True:     
        limpar_tela()
        registros = ler_lista_em_json(nome_arquivo)
        nome = input(f"Informe o código da {entidade}: ").strip()
        cpf = input(f"Informe o código do professor referente {entidade}: ").strip()
        codigo = input(f"Informe o código da disciplina referente a {entidade}: ").strip()

        if codigo in registros:
            print("Já existe uma turma com este código.")
            input("Pressione ENTER para continuar...")
            continue

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

#Função para poder incluir os dados os arquivos para o tópico das matrículas
            
def incluir_registro_matriculas(nome_arquivo, entidade):
    while True:     
        limpar_tela()
        registros = ler_lista_em_json(nome_arquivo)
        nome = input(f"Informe o código da {entidade}: ").strip()
        codigo = input(f"Informe o código do estudante referente a {entidade}: ").strip()
        
        if codigo in registros:
            print("Já existe uma turma com este código.")
            input("Pressione ENTER para continuar...")
            continue

        if not codigo.isdigit():
            print("Código inválido. Deve ser numérico.")
        elif not re.match(r"^[A-Za-zÀ-ÿ\s]+$", nome):
            print("Erro: O nome não pode conter números ou caracteres especiais.")
        else:
            registros[(codigo)] = {
                "nome": nome
            }
            escrever_lista_em_json(registros, nome_arquivo)
            input(f"\n{entidade.capitalize()} cadastrado com sucesso! Pressione ENTER para continuar...")
            if input("Deseja adicionar outro? (s/n): ").lower() == 'n':
                break

#Função para poder listar os dados dos tópicos

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
    
#Função para poder listar os dados do tópico "turmas"
    
def listar_registros_turmas(nome_arquivo, entidade):
    limpar_tela()
    registros = ler_lista_em_json(nome_arquivo)
    if not registros:
        print(f"Não há {entidade}s cadastrados.")
    else:
        print(f"Lista de {entidade}s:")
        for codigo, dados in registros.items():
            print(f"Código Turmas - {codigo:<10} | Código Prof - {dados['nome']:<20} | Código Disc - {dados['cpf']:<14}")
    input("\nPressione ENTER para continuar...")

#Função para poder listar os dados do tópico "matrículas"
    
def listar_registros_matriculas(nome_arquivo, entidade):
    limpar_tela()
    registros = ler_lista_em_json(nome_arquivo)
    if not registros:
        print(f"Não há {entidade}s cadastrados.")
    else:
        print(f"Lista de {entidade}s:")
        for codigo, dados in registros.items():
            print(f"Código Matriculas - {codigo:<10} | Código Estudante - {dados['nome']:<20}")
    input("\nPressione ENTER para continuar...")
    
#Função para atualizar os dados dos tópicos

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
    
#Função para atualizar os dados dos tópico "disciplinas"
    
def atualizar_registro_disciplinas(nome_arquivo, entidade):
    limpar_tela()
    registros = ler_lista_em_json(nome_arquivo)
    cod = input(f"Informe o código do(a) {entidade} que deseja atualizar: ").strip()
    if cod in registros:
            novo_nome = input("Informe o novo nome: ").strip()
            novo_codigo = input("Informe o novo código: ").strip()

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
                escrever_lista_em_json(registros, nome_arquivo)
                print("Dados atualizados com sucesso!")       
    else:
        print("Código inválido. Deve ser um número.")
    input("\nPressione ENTER para continuar...")
    
#Função para atualizar os dados dos tópico "matriculas"
    
def atualizar_registro_matriculas(nome_arquivo, entidade):
    limpar_tela()
    registros = ler_lista_em_json(nome_arquivo)
    cod = input(f"Informe o código do(a) {entidade} que deseja atualizar: ").strip()
    if cod in registros:
            novo_nome = input("Informe o novo nome: ").strip()
            novo_codigo = input("Informe o novo código: ").strip()

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
                escrever_lista_em_json(registros, nome_arquivo)
                print("Dados atualizados com sucesso!")       
    else:
        print("Código inválido. Deve ser um número.")
    input("\nPressione ENTER para continuar...")
    
#Função para excluir os dados dos tópicos

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
    
#While que funciona como menu para executar os comandados.

while True:
    limpar_tela()
    print("---- MENU PRINCIPAL ----")
    print("(1) Gerenciar Estudantes ")
    print("(2) Gerenciar Professores ")
    print("(3) Gerenciar Disciplinas ")
    print("(4) Gerenciar Turmas ")
    print("(5) Gerenciar Matrículas ")
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
        while True:
            limpar_tela()
            print("** [PROFESSORES] MENU DE OPERACOES **")
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Atualizar.")
            print("(4) Excluir.")
            print("(5) Voltar ao menu principal.")

            opcao_aluno = input("Digite a opção: ")
    
            if opcao_aluno == "1":
                incluir_registro(arquivo_professores, "professor")
            elif opcao_aluno == "2":
                listar_registros(arquivo_professores, "professor")
            elif opcao_aluno == "3":
                atualizar_registro(arquivo_professores, "professor")
            elif opcao_aluno == "4":
                excluir_registro(arquivo_professores, "professor")
            elif opcao_aluno == "5":
                break
            else:
                print("Opção inválida.")
                input("Pressione ENTER...")

    elif opcao == "3":
        while True:
            limpar_tela()
            print("** [DISCIPLINAS] MENU DE OPERACOES **")
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Atualizar.")
            print("(4) Excluir.")
            print("(5) Voltar ao menu principal.")

            opcao_aluno = input("Digite a opção: ")

            if opcao_aluno == "1":
                incluir_registro_disciplina(arquivo_disciplinas, "disciplina")
            elif opcao_aluno == "2":
                listar_registros(arquivo_disciplinas, "disciplina")
            elif opcao_aluno == "3":
                atualizar_registro_disciplinas(arquivo_disciplinas, "disciplina")
            elif opcao_aluno == "4":
                excluir_registro(arquivo_disciplinas, "disciplina")
            elif opcao_aluno == "5":
                break
            else:
                print("Opção inválida.")
                input("Pressione ENTER...")

    elif opcao == "4":
        while True:
            limpar_tela()
            print("** [TURMAS] MENU DE OPERACOES **")
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Atualizar.")
            print("(4) Excluir.")
            print("(5) Voltar ao menu principal.")

            opcao_aluno = input("Digite a opção: ")

            if opcao_aluno == "1":
                incluir_registro_turmas(arquivo_turmas, "turmas")
            elif opcao_aluno == "2":
                listar_registros_turmas(arquivo_turmas, "turmas")
            elif opcao_aluno == "3":
                atualizar_registro(arquivo_turmas, "turmas")
            elif opcao_aluno == "4":
                excluir_registro(arquivo_turmas, "turmas")
            elif opcao_aluno == "5":
                break
            else:
                print("Opção inválida.")
                input("Pressione ENTER...")

    elif opcao == "5":
        while True:
            limpar_tela()
            print("** [MATRÍCULAS] MENU DE OPERACOES **")
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Atualizar.")
            print("(4) Excluir.")
            print("(5) Voltar ao menu principal.")

            opcao_aluno = input("Digite a opção: ")

            if opcao_aluno == "1":
                incluir_registro_matriculas(arquivo_matriculas, "matricula")
            elif opcao_aluno == "2":
                listar_registros_matriculas(arquivo_matriculas, "matricula")
            elif opcao_aluno == "3":
                atualizar_registro_matriculas(arquivo_matriculas, "matricula")
            elif opcao_aluno == "4":
                excluir_registro(arquivo_matriculas, "matricula")
            elif opcao_aluno == "5":
                break
            else:
                print("Opção inválida.")
                input("Pressione ENTER...")

    elif opcao == "9":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
        input("\nPressione ENTER para continuar...")