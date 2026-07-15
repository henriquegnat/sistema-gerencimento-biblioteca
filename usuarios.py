from auxiliares import limpar_terminal, verificar_usuarios, escolher_usuario
from dados import usuarios

def cadastrar_usuarios():
    limpar_terminal()
    print("===CRIAÇÃO DE USUÁRIO===")
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite o cpf do usuario: ")
    data_nascimento = input("Digite a data de nascimento do usuário ")

    usuario = {}
    usuario["nome"] = nome
    usuario["cpf"] = cpf
    usuario["data_nascimento"] = data_nascimento
    usuarios.append(usuario)

def listar_usuarios():
    if verificar_usuarios():
        print("====USUARIOS====")
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. {usuario['nome'].upper()}")
            print("CPF:", usuario["cpf"])
            print("Data de Nascimento:", usuario["data_nascimento"])
            print('--------------')

def remover_usuarios():
    limpar_terminal()
    if verificar_usuarios():
        listar_usuarios()
        usuario = escolher_usuario()
        if usuario:
            usuarios.pop(usuario.index(usuario))
            print("\nLivro removido com sucesso!")
