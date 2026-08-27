from persistencia import salvar_locacoes, carregar_locacoes

locacoes = []

def cadastrar_locacoes(jogo, dias, cliente):
    valor = jogo['valor']
    desconto = 0

    if dias > 7:
        desconto = valor * 0.1
    elif dias > 3:
        desconto = valor * 0.05

    locacao = {'jogo': jogo, 'dias': dias, 'total': (valor - desconto), 'cliente': cliente}

    locacoes.append(locacao)
    salvar_locacoes(locacoes)

def listar_locacoes():
    locacoes = carregar_locacoes()
    for indice, locacao in enumerate(locacoes, start=1):
        print(indice, "-", locacao)
