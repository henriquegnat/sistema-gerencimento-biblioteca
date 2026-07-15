from dados import livros
from auxiliares import limpar_terminal, escolher_livro, verificar_livros

def cadastrar_livros():
    limpar_terminal()
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
    limpar_terminal()
    if verificar_livros():
        listar_livros()

        livro = escolher_livro()
        if livro:
            livros.pop(livros.index(livro))
            print("\nLivro removido com sucesso!")

def editar_livro():
    limpar_terminal()
    if verificar_livros():
        listar_livros()
        livro = escolher_livro()

        if livro:
            while True:
                print("1. Nome"
                      "\n2. Autor"
                      "\n3. Genero"
                      "\n4. Cópias Totais"
                      "\n5. Escolher outro livro"
                      "\n0. Voltar para o menu")
                escolha_livro = input("\nDigite o que você deseja mudar! ")

                if escolha_livro.isdigit() and '1' <= escolha_livro <= '4':
                    if escolha_livro == '1':
                        novo_nome = input("Qual será o novo nome do livro? ")
                        livro['nome'] = novo_nome
                        print("Livro reenomeiado com sucesso!")
                        break

                    elif escolha_livro == '2':
                        novo_autor = input("Qual será o novo nome do autor? ")
                        livro['autor'] = novo_autor
                        print("Autor reenomeiado com sucesso!")
                        break

                    elif escolha_livro == '3':
                        novo_genero = input("Qual será o gênero do livro? ")
                        livro['genero'] = novo_genero
                        print("Gênero reenomeiado com sucesso!")
                        break

                    elif escolha_livro == '4': #colocar verificao de numero de copias!!
                        novo_copias = input("\nQual será a nova quantidade de cópias totais do livro? ")
                        if novo_copias.isdigit(): #verificando se novo_copias é número
                            novo_copias = int(novo_copias)
                            emprestimos = livro['copias_totais'] - livro["copias_disponiveis"]

                            if novo_copias > livro['copias_totais']: #SE AUMENTAR
                                livro['copias_disponiveis'] = livro['copias_disponiveis'] + (novo_copias - livro['copias_totais'])
                                livro['copias_totais'] = novo_copias
                                print("Cópias Totais alteradas com sucesso!")
                                break

                            elif novo_copias < livro['copias_totais']: #SE DIMINUIR
                                if novo_copias < emprestimos: #não pode ser menor que a quantidade de EMPRÉSTIMOS
                                    print('\nEssa ação não pode ser feita!\n'
                                          'Por favor digite um número válido\n')
                                else:
                                    livro['copias_disponiveis'] = livro['copias_disponiveis'] - (livro['copias_totais'] - novo_copias)
                                    print("PRINT")
                                    livro['copias_totais'] = novo_copias
                                    print("Cópias Totais alteradas com sucesso!")
                                    break

                            elif novo_copias == livro['copias_totais']:
                                print("Novo número de cópias igual ao existente."
                                      "\nDigite outro valor válido!")



                elif escolha_livro == '5':
                    listar_livros()
                    escolher_livro()

                elif escolha_livro == '0':
                    break

                else:
                    print("Digite um número válido!")

def buscar_livro():
    limpar_terminal()
    if verificar_livros():
        pesquisa = input("\nQual livro você deseja buscar?")
        busca = []
        for livro in livros:
            if pesquisa.lower() in livro['nome'].lower():
                busca.append(livro)

        if not busca:
            print("Nenhum Livro encontrado!")
            return

        print('\nRESULTADOS ENCONTRADOS:')
        for i, livro in enumerate(busca, start=1):

            print(f"{i}. {livro['nome'].upper()}")
            print("Autor:", livro["autor"])
            print("Gênero:", livro["genero"])
            print("Cópias:", livro["copias_disponiveis"],"/",livro["copias_totais"], "disponíveis no momento!")
            print('--------------')