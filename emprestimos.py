from auxiliares import limpar_terminal, verificar_livros, escolher_livro
from livros import listar_livros

def emprestar_livro():
    limpar_terminal()
    if verificar_livros():
        listar_livros()
        livro = escolher_livro()

        if livro:
            if livro["copias_disponiveis"] == 0: print("\nLivro não disponível para empréstimo!")
            else: livro["copias_disponiveis"] = livro["copias_disponiveis"] - 1; print("\nLivro Emprestado com Sucesso!")

def devolver_livro():
    limpar_terminal()
    if verificar_livros():
        listar_livros()

        livro = escolher_livro()
        if livro["copias_disponiveis"] < (livro["copias_totais"]):
            livro["copias_disponiveis"] = livro["copias_disponiveis"] + 1
            print("\nLivro Devolvido com Sucesso!")
        else:
            print("\nEsse livro não pode ser devolvido!")