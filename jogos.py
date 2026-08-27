from persistencia import salvar_jogos, carregar_jogos

plataformas = ["PLAYSTATION", "PC", "NINTENDO", "XBOX"]

jogos = []

def cadastrar_jogo(titulo, genero, plataforma, valor, estoque):
    jogo = {}
    if plataforma == 1:
        jogo = {'titulo': titulo, 'genero': genero, 'plataforma': 'Playstation', 'valor': valor, 'estoque': estoque}
    elif plataforma == 2:
        jogo = {'titulo': titulo, 'genero': genero, 'plataforma': 'Pc', 'valor': valor, 'estoque': estoque}
    elif plataforma == 3:
        jogo = {'titulo': titulo, 'genero': genero, 'plataforma': 'Nintendo', 'valor': valor, 'estoque': estoque}
    elif plataforma == 4:
        jogo = {'titulo': titulo, 'genero': genero, 'plataforma': 'Xbox', 'valor': valor, 'estoque': estoque}
    jogos.append(jogo)
    salvar_jogos(jogos)

def listar_jogos():
    jogos = carregar_jogos()
    for indice, jogo in enumerate(jogos, start=1):
        print(indice, "-", jogo)