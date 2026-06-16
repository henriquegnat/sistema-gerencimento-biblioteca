print("Bem vindo ao Sistema de Gerenciamento de Biblioteca!")


livros = []

def exibir_menu():
    print("====MENU====")
    print("1. Cadastrar livros")
    print("2. Listar livros")
    print("3. Remover livro")
    print("4. Sair")

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
        break
    else:
        print("Digite um valor valido!")