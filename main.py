print("Bem vindo ao Sistema de Gerenciamento de Biblioteca!")

livros = []

def exibir_menu():
    print("====MENU====")
    print("1. Cadastrar livros")
    print("2. Listar livros")
    print("3. Remover livro")
    print("4. Editar Livros")
    print("5. Buscar Livros")
    print("6. Sair")

def cadastrar_livros():
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    genero = input("Digite o genero do livro: ")

    livro = {}
    livro["nome"] = nome
    livro["autor"] = autor
    livro["genero"] = genero
    livros.append(livro)

def listar_livros():
    if len(livros) == 0:
        print("Nenhum livro cadastrado!")

    else:
        print("====LIVROS====")
        for i, livro in enumerate(livros, start=1):
            print('--------------')
            print(f"{i}. {livro['nome'].upper()}")
            print("Autor:", livro["autor"])
            print("Gênero:", livro["genero"])
            print('--------------')

def remover_livros():
    if len(livros) == 0:
        print("Nenhum livro cadastrado!")
        return

    print("====LIVROS CADASTRADOS====")
    for i, livro in enumerate(livros, start=1): #enumera os elementos da lista livros, começando 1, 2,3 ....
        print(f"{i}° Livro: {livro['nome']}")

    while True:
        escolha = input("Qual livro vc deseja remover?")
        if escolha.isdigit(): #Metodo de string para verificar se oq está escrito é numero
            escolha = int(escolha)
            if escolha > 0  and escolha <= len(livros):
                remover = escolha - 1
                livros.pop(remover)
                print("Livro removido com sucesso!")
                break
            else:
                print("Número digitado inválido!")
        else:
            print("Digite um valor valido!")

def editar_livro():
    print("====LIVROS======")
    if len(livros) == 0:
        print("Nenhum livro cadastrado!")
        return

    for i, livro in enumerate(livros, start=1):
        print(f"{i}° Livro: {livro['nome']}")

    while True:
        escolher_livro = input("Qual livro você deseja editar?")
        if escolher_livro.isdigit():
            escolher_livro = int(escolher_livro)
            if escolher_livro > 0 and escolher_livro <= (len(livros)):
                indice_livro= escolher_livro - 1
                livro_editado = livros[indice_livro] # Associa a variável ao dicionário do livro escolhido na lista
                novo_nome = input("Qual será o novo nome do livro??")
                livro_editado['nome'] = novo_nome
                print("Livro reenomeiado com sucesso!")
                break
            else:
                print("Número digitado inválido!")

        else:
            print("Digite um valor valido!")


def buscar_livro():
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
        print('--------------')

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
        break
    else:
        print("Digite um valor valido!")