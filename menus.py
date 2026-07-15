from livros import cadastrar_livros,listar_livros,remover_livros,editar_livro,buscar_livro
from usuarios import cadastrar_usuarios, listar_usuarios, remover_usuarios, editar_usuario
from emprestimos import emprestar_livro, devolver_livro
from auxiliares import limpar_terminal

def exibir_menuPrincipal():
    print("\n====MENU PRINCIPAL====")
    print("1. Gerenciar Livros")
    print("2. Gerenciar Usuários")
    print("3. Gerenciar Empréstimos")
    print("0. Salvar e Sair")

def exibir_menuLivros():
    while True:
        print("\n===LIVROS====")
        print("1. Cadastrar livros")
        print("2. Listar livros")
        print("3. Remover livro")
        print("4. Editar Livros")
        print("5. Buscar Livros")
        print("0. Voltar ao Menu Principal")
        escolha_livro = (input("\nO que deseja fazer? "))

        if escolha_livro == '1':
            cadastrar_livros()
        if escolha_livro == '2':
            limpar_terminal()
            listar_livros()
        if escolha_livro == '3':
            remover_livros()
        if escolha_livro == '4':
            editar_livro()
        if escolha_livro == '5':
            buscar_livro()
        if escolha_livro == '0':
            break


def exibir_menuUsuarios():
    limpar_terminal()
    while True:
        print("\n===USUARIOS====")
        print("1. Cadastrar Usuários")
        print("2. Listar Usuário")
        print("3. Remover Usuários")
        print("4. Editar Usuários")
        print("5. Buscar Usuários")
        print("0. Voltar ao Menu Principal")
        escolha_usuario = (input("\nO que deseja fazer? "))

        if escolha_usuario == '1':
            cadastrar_usuarios()
        if escolha_usuario == '2':
            limpar_terminal()
            listar_usuarios()
        if escolha_usuario == '3':
            remover_usuarios()
        if escolha_usuario == '4':
            editar_livro()
        if escolha_usuario == '5':
            buscar_livro()
        if escolha_usuario == '0':
            break

def exibir_menuEmprestimos():
    while True:
        print("\n===EMPRÉSTIMOS====")
        print("1. Emprestar Livro")
        print("2. Devolver Livro")
        print("0. Voltar ao Menu Principal")
        escolha_emprestimo = (input("\nO que deseja fazer? "))

        if escolha_emprestimo == '1':
            emprestar_livro()
        if escolha_emprestimo == '2':
            devolver_livro()
        if escolha_emprestimo == '0':
            break