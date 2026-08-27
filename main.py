from persistencia import carregar_jogos, carregar_clientes, carregar_locacoes
from jogos import jogos, plataformas, cadastrar_jogo, listar_jogos
from clientes import cadastrar_clientes, listar_clientes
from locacoes import cadastrar_locacoes, listar_locacoes

def menu_jogos():
    print("-"*5, "MENU DE JOGOS", "-"*5)
    print("1 - Cadastrar jogos")
    print("2 - Listar jogos")

    opcao2 = input("Digite a opção que deseja realizar: ")

    if opcao2 == '1':
        print("Plataformas:")
        for indice, plataforma in enumerate(plataformas, start=1):
            print(indice, "-", plataforma)
        plataforma_escolhida = int(input("Escolha: ")) - 1
        titulo = input("Informe o título do jogo: ")
        genero = input("Informe o gênero: ")
        valor = float(input("Informe o valor de locação: "))
        estoque = int(input("Informe o estoque inicial: "))
        cadastrar_jogo(titulo, genero, plataforma_escolhida, valor, estoque)

    elif opcao2 == '2': 
        listar_jogos()

def menu_clientes():
    print("-"*5, "MENU DE CLIENTES", "-"*5)
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")

    opcao3 = input("Digite a opção que deseja realizar: ")

    if opcao3 == '1':
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu cpf: ")
        telefone = input("Digite seu telefone: ")
        cadastrar_clientes(nome, cpf, telefone)

    elif opcao3 == '2':
        listar_clientes()

def menu_locacoes():
    print("-"*5, "MENU DE LOCAÇÕES", "-"*5)
    print("1 - Realizar locações")
    print("2 - Listar locações")

    opcao4 = input("Digite a opção que deseja realizar: ")

    if opcao4 == '1':
        listar_jogos()
        id_jogo = int(input("Digite qual o id do jogo que você deseja alugar: "))
        listar_clientes()
        cliente = input("Digite seu cpf: ")
        dias = int(input("Digite por quantos dias você vai ficar com esse jogo: "))
        jogo = jogos[id_jogo-1]
        if jogo['estoque'] <= 0:
            print("Esse jogo não está disponível.")
            return
        jogo['estoque'] -= 1
        cadastrar_locacoes(jogo, dias, cliente)

    elif opcao4 == '2':
        listar_locacoes()
        
jogos = carregar_jogos()
clientes = carregar_clientes()
locacoes = carregar_locacoes()
while(True):
    print("="*15, "MENU", "="*15)
    print("1 - Jogos")
    print("2 - Clientes")
    print("3 - Locações")
    print("4 - Sair")

    opcao = input("Digite a opção que deseja realizar: ")

    if opcao == '1':
        menu_jogos()

    elif opcao == '2':
        menu_clientes()

    elif opcao == '3':
        menu_locacoes()

    elif opcao == '4':
        break

    else:
        print("Erro, tente novamente.")
        continue