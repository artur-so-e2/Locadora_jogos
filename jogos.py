from persistencia import salvar_jogos, carregar_jogos

plataformas = ["XBOX", "PC", "NINTENDO", "PLAYSTAION"]

jogos = []

def cadastrar_jogo(titulo, genero, plataforma, valor, estoque):
    jogo = {'titulo': titulo, 'genero': genero, 'plataforma': plataforma, 'valor': valor, 'estoque': estoque}
    jogos.append(jogo)
    salvar_jogos(jogos)

def listar_jogos():
    jogos = carregar_jogos()
    for indice, jogo in enumerate(jogos, start=1):
        print(indice, "-", jogo)