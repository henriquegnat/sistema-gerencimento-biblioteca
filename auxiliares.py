import os
from dados import livros, usuarios

def escolher_livro():
    limpar_terminal()
    while True:
        escolher_livro = input("\nQual livro você deseja selecionar? (Se deseja voltar, digite 0) ")
        if escolher_livro.isdigit():
            escolher_livro = int(escolher_livro)
            if escolher_livro > 0 and escolher_livro <= (len(livros)):  # entre 1 e o numero de livros da lista
                indice_livro = escolher_livro - 1
                livro_emprestado = livros[indice_livro]
                return livro_emprestado
            elif escolher_livro == 0:
                return None
            else:
                print("Número digitado inválido!")
        else:
            print("Número digitado inválido!")

def verificar_livros():
    if len(livros) == 0:
        print("\nNenhum livro cadastrado!")
        return False
    return True

def verificar_usuarios():
    if len(usuarios) == 0:
        print("\nNenhum usuario cadastrado!")
        return False
    return True

def escolher_usuario():
    while True:
        escolha_usuario = input("\nQual usuário você deseja selecionar? (Se deseja voltar, digite 0) ")
        if escolha_usuario.isdigit():
            escolha_usuario = int(escolha_usuario)
            print(escolha_usuario)
            if escolha_usuario > 0 and escolha_usuario <= (len(usuarios)):      #entre 1 e o numero de livros da lista
                indice_usuario = escolha_usuario - 1
                usuario_escolhido = usuarios[indice_usuario]
                return usuario_escolhido
            elif escolher_livro == 0:
                return None
            else:
                print("Número digitado inválido!!me a")
        else:
            print("Número digitado inválido! oie")


def limpar_terminal():
    os.system("cls") # comando pro windows ou linux/mac

