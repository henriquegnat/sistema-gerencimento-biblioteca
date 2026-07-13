import json

print("Bem vindo ao Sistema de Gerenciamento de Biblioteca!")

def carregar_dados():
    try:
        with open("livros.json", "r") as arquivos:
            dados = json.load(arquivos)
            print("Dados carregados com sucesso!!")
            return dados
    except:
        return []

livros = carregar_dados()

def verificar_livros():
    if len(livros) == 0:
        print("Nenhum livro cadastrado!")
        return False
    return True

def escolher_livro():
    while True:
        escolher_livro = input("Qual livro você deseja selecionar? ")
        if escolher_livro.isdigit():
            escolher_livro = int(escolher_livro)
            if escolher_livro > 0 and escolher_livro <= (len(livros)):  # entre 1 e o numero de livros da lista
                indice_livro = escolher_livro - 1
                livro_emprestado = livros[indice_livro]
                return livro_emprestado
            else:
                print("Número digitado inválido!")
        else:
            print("Número digitado inválido!")



def exibir_menu():
    print("====MENU====")
    print("1. Cadastrar livros")
    print("2. Listar livros")
    print("3. Remover livro")
    print("4. Editar Livros")
    print("5. Buscar Livros")
    print("6. Emprestar Livros")
    print("7. Devolver Livros")
    print("8. Salvar e Sair")

def cadastrar_livros():
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    genero = input("Digite o genero do livro: ")
    copias_totais = input("Digite o número de cópias totais do livro: ")
    while True:
        if copias_totais.isdigit():
            livro = {}
            livro["nome"] = nome
            livro["autor"] = autor
            livro["genero"] = genero
            livro["copias_totais"] = int(copias_totais)
            livro["copias_disponiveis"] = int(copias_totais)
            livros.append(livro)
            break
        else:
            print("Digite um número!")
            copias_totais = input("Digite o número de cópias totais do livro: ")

def listar_livros():
    if verificar_livros():
        print("====LIVROS====")
        for i, livro in enumerate(livros, start=1):
            print(f"{i}. {livro['nome'].upper()}")
            print("Autor:", livro["autor"])
            print("Gênero:", livro["genero"])
            print("Cópias:", livro["copias_disponiveis"],"/",livro["copias_totais"], "disponíveis no momento!")
            print('--------------')

def remover_livros():
    if verificar_livros():
        listar_livros()

        livro = escolher_livro()
        livros.pop(livros.index(livro))
        print("Livro removido com sucesso!")


def editar_livro():
    if verificar_livros():
        listar_livros()

        livro = escolher_livro()

        novo_nome = input("Qual será o novo nome do livro? ")
        livro['nome'] = novo_nome
        print("Livro reenomeiado com sucesso!")



def buscar_livro():
    if verificar_livros():
        pesquisa = input("Qual livro você deseja buscar?")
        busca = []
        for livro in livros:
            if pesquisa.lower() in livro['nome'].lower():
                busca.append(livro)

        if not busca:
            print("Nenhum Livro encontrado!")
            return

        print('RESULTADOS ENCONTRADOS:')
        for i, livro in enumerate(busca, start=1):

            print(f"{i}. {livro['nome'].upper()}")
            print("Autor:", livro["autor"])
            print("Gênero:", livro["genero"])
            print("Cópias:", livro["copias_disponiveis"],"/",livro["copias_totais"], "disponíveis no momento!")
            print('--------------')

def salvar_dados():
    with open("livros.json", "w") as arquivo:
        json.dump(livros, arquivo)
        print("Dados salvos com sucesso!")

def emprestar_livro():
    if verificar_livros():
        listar_livros()
        livro = escolher_livro()

        if livro["copias_disponiveis"] == 0: print("Livro não disponível para empréstimo!")
        else: livro["copias_disponiveis"] = livro["copias_disponiveis"] - 1; print("Livro Emprestado com Sucesso!")




def devolver_livro():
    if verificar_livros():
        listar_livros()

        livro = escolher_livro()
        if livro["copias_disponiveis"] < (livro["copias_totais"]):
            livro["copias_disponiveis"] = livro["copias_disponiveis"] + 1
            print("Livro Devolvido com Sucesso!")
        else:
            print("\nEsse livro não pode ser devolvido!")


while True:
    exibir_menu()
    escolha = (input("O que deseja fazer? "))
    if escolha == "1":
        cadastrar_livros()
    elif escolha == "2":
        listar_livros()
    elif escolha == "3":
        remover_livros()
    elif escolha == "4":
        editar_livro()
    elif escolha == "5":
        buscar_livro()
    elif escolha == "6":
        emprestar_livro()
    elif escolha == "7":
        devolver_livro()
    elif escolha == "8":
        salvar_dados()
        break
    else:
        print("Digite um valor valido!")