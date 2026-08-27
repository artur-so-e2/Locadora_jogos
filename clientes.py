from persistencia import salvar_clientes, carregar_clientes

clientes = []

def cadastrar_clientes(nome, cpf, telefone):
    cliente = {'nome': nome, 'cpf': cpf, 'telefone': telefone}

    clientes.append(cliente)
    salvar_clientes(clientes)

def listar_clientes():
    clientes = carregar_clientes()
    for indice, cliente in enumerate(cliente, start=1):
        print(indice, "-", cliente)