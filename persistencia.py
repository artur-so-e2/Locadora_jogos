import json

def salvar_jogos(jogos):
    with open("jogos.json", "w", encoding="utf-8") as arquivo:
        json.dump(jogos, arquivo)

def carregar_jogos():
    try:
        with open("jogos.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
            return []


def salvar_clientes(clientes):
    with open("clientes.json", "w", encoding="utf-8") as arquivo:
        json.dump()

def carregar_clientes():
    try:
        with open("clientes.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
            return []


def salvar_locacoes(locacoes):
    with open("locacoes.json", "w", encoding="utf-8") as arquivo:
        json.dump(locacoes, arquivo)

def carregar_locacoes():
    try:
        with open("locacoes.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
            return []