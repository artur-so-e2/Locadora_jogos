from persistencia import carregar_jogos, carregar_clientes, carregar_locacoes
from locacoes import cadastrar_locacoes
from jogos import jogos, plataformas, cadastrar_jogo, listar_jogos

def menu_jogos():
    opcao = input("Digite 1-Cadastrar 2-Listar: ")
    if (opcao == '1'):
        print("Plataformas:")
        for indice, plataforma in enumerate(plataformas, start=1):
            print(indice, "-", plataforma)
        plataforma_escolhida = int(input("Escolha: ")) - 1
        titulo = input("Informe o título do jogo: ")
        genero = input("Informe o gênero: ")
        valor = float(input("Informe o valor de locação: "))
        estoque = int(input("Informe o estoque inicial: "))
        cadastrar_jogo(titulo, genero, plataforma_escolhida, valor, estoque)

    elif opcao == '2':
        carregar_jogos()

def menu_locacoes():
    opcao = input("Digite 1-Realizar locação 2-Listar locações: ")
    if (opcao == '1'):
        listar_jogos()
        id_jogo = int(input("Digite qual o id do jogo que você deseja alugar: "))
        dias = int(input("Digite por quantos dias você vai ficar com esse jogo: "))
        jogo = jogos[id_jogo-1]
        if jogo['estoque'] <= 0:
            print("Esse jogo não está disponível.")
            return
        jogo['estoque'] -= 1
        cadastrar_locacoes(jogo, dias)
        



jogos = carregar_jogos()
while(True):
    print("="*15, "MENU", "="*15)
    print("1 - Jogos")
    print("2 - Listar jogos")
    print("3 - Cadastrar clientes")
    print("4 - Listar clientes")
    print("5 - Locações")
    print("7 - Sair")

    opcao = input("Digite a opção que deseja realizar: ")

    if opcao == '1':
        menu_jogos()

    elif opcao == '2':
        carregar_jogos()

    elif opcao == '3':
        pass

    elif opcao == '4':
        carregar_clientes()

    elif opcao == '5':
        menu_locacoes()

    elif opcao == '6':
        jogo = input("Digite qual o id do jogo que você deseja alugar: ")
        dias = int(input("Digite por quantos dias você vai ficar com esse jogo: "))
        for game in jogos:
            if unidades > 0:
                carregar_locacoes(jogo, dias)
                unidades -= 1
                print("Locação realizada com sucesso.")

    elif opcao == '7':
        break

    else:
        print("Erro, tente novamente.")
        continue