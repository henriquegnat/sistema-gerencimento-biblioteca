import json


def carregar_dados():
    try:
        with open("livros.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            print("Dados carregados com sucesso!")
            return dados

    except FileNotFoundError:
        return {
            "livros": [],
            "usuarios": [],
            "emprestimos": []
        }


dados = carregar_dados()

livros = dados["livros"]
usuarios = dados["usuarios"]


def salvar_dados():
    dados = {
        "livros": livros,
        "usuarios": usuarios
    }

    with open("livros.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    print("Dados salvos com sucesso!")