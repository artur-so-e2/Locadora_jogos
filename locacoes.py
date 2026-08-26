from persistencia import salvar_locacoes

locacoes = []

def cadastrar_locacoes(jogo, dias):
    valor = jogo['valor']
    desconto = 0

    if dias > 7:
        desconto = valor * 0.1
    elif dias > 3:
        desconto = valor * 0.05

    locacao = {'jogo': jogo, 'dias': dias, 'total': (valor - desconto)}

    locacoes.append(locacao)
    salvar_locacoes(locacoes)