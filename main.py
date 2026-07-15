from auxiliares import limpar_terminal
from dados import salvar_dados
from menus import exibir_menuPrincipal, exibir_menuLivros, exibir_menuUsuarios, exibir_menuEmprestimos

print("Bem vindo ao Sistema de Gerenciamento de Biblioteca!")

while True:
    limpar_terminal()
    exibir_menuPrincipal()
    escolha = (input("\nO que deseja fazer? "))
    if escolha == "1":
        limpar_terminal()
        exibir_menuLivros()
    elif escolha == "2":
        limpar_terminal()
        exibir_menuUsuarios()
    elif escolha == "3":
        limpar_terminal
        exibir_menuEmprestimos()
    elif escolha == "0":
        salvar_dados()
        break
    else:
        print("Digite um valor valido!")
        