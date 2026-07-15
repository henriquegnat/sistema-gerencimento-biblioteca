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
        limpar_terminal()
        return False
    return True

def verificar_usuarios():
    if len(usuarios) == 0:
        print("\nNenhum usuario cadastrado!")
        limpar_terminal()
        return False
    return True

def escolher_usuario():
    limpar_terminal()
    while True:
        escolher_usuario = input("\nQual usuário você deseja selecionar? (Se deseja voltar, digite 0) ")
        if escolher_usuario.isdigit():
            escolher_usuario = int(escolher_usuario)
            if escolher_usuario > 0 and escolher_usuario <= (len(livros)):  # entre 1 e o numero de livros da lista
                indice_usuario = escolher_usuario - 1
                usuario_escolhido = usuarios[indice_usuario]
                return usuario_escolhido
            elif escolher_livro == 0:
                return None
            else:
                print("Número digitado inválido!")
        else:
            print("Número digitado inválido!")
def limpar_terminal():
    os.system("cls") # comando pro windows ou linux/mac

