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
            usuarios.pop(usuarios.index(usuario))
            print("\nLivro removido com sucesso!")

def editar_usuario():
    limpar_terminal()
    if verificar_usuarios():
        listar_usuarios()
        usuario = escolher_usuario()

        if usuarios:
            while True:
                print("\n. Nome"
                      "\n2. Autor"
                      "\n3. Genero"
                      "\n0. Voltar para o menu")
                escolha_usuario = input("\nDigite o que você deseja mudar! ")

                if escolha_usuario.isdigit() and '1' <= escolha_usuario <= '3':
                    if escolha_usuario == '1':
                        novo_nome = input("Qual será o novo nome do livro? ")
                        usuario['nome'] = novo_nome
                        print("Usuário reenomeiado com sucesso!")
                        break

                    elif escolha_usuario == '2':
                        novo_cpf = input("Qual será o novo CPF do usuário? ")
                        usuario['cpf'] = novo_cpf
                        print("CPF auterado com sucesso! com sucesso!")
                        break

                    elif escolha_usuario == '3':
                        novo_data_nascimento = input("Qual será a nova data de nascimento do usuário? ")
                        usuario['data_nascimento'] = novo_data_nascimento
                        print("Data de Nascimento alterada com sucesso!")
                        break

                    elif escolha_usuario == '0':
                        break

                else:
                    print("Digite um número válido!")