from typing import List

# Armazenamento de dados
usuarios = []
contas = []
contador_contas = 1

# Funções para cadastro
def cadastrar_usuario(nome: str, data_nascimento: str, cpf: str, endereco: str):
    cpf_numeros = ''.join([c for c in cpf if c.isdigit()])
    for usuario in usuarios:
        if usuario['cpf'] == cpf_numeros:
            print("Erro: CPF já cadastrado.")
            return
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf_numeros, 'endereco': endereco})
    print(f"Usuário {nome} cadastrado com sucesso.")

def cadastrar_conta(cpf: str):
    global contador_contas
    cpf_numeros = ''.join([c for c in cpf if c.isdigit()])
    usuario = next((u for u in usuarios if u['cpf'] == cpf_numeros), None)
    if not usuario:
        print("Erro: Usuário não encontrado.")
        return
    contas.append({'agencia': '0001', 'numero_conta': contador_contas, 'usuario': usuario, 'saldo': 0.0, 'extrato': [], 'numero_saques': 0})
    print(f"Conta {contador_contas} vinculada ao usuário {usuario['nome']}.")
    contador_contas += 1

# Função de depósito (recebe por posição)
def deposito(saldo_bancario: float, valor: float, extrato: List[float]):
    saldo_bancario += valor
    extrato.append(valor)
    return saldo_bancario, extrato

# Função de saque (recebe por nome)
def saque(*, saldo_bancario: float, valor: float, extrato: List[float], limite: float, numero_saques: int, limite_saques: int):
    if valor > saldo_bancario:
        print("Saldo insuficiente.")
        return saldo_bancario, extrato
    elif numero_saques >= limite_saques:
        print("Limite de saques diários atingido.")
        return saldo_bancario, extrato
    elif valor > limite:
        print("Valor do saque excede o limite permitido.")
        return saldo_bancario, extrato
    saldo_bancario -= valor
    extrato.append(-valor)
    return saldo_bancario, extrato

# Função de extrato (recebe por posição e nome)
def exibir_extrato(saldo: float, *, extrato: List[float]):
    print(f"Saldo atual: R$ {saldo:.2f}")
    if not extrato:
        print("Nenhuma movimentação registrada.")
    else:
        print("Extrato:")
        for movimento in extrato:
            print(f"R$ {movimento:.2f}")

# Função para listar todos os usuários
def listar_usuarios() -> dict:
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return None
    print("Usuários disponíveis:")
    for idx, usuario in enumerate(usuarios):
        print(f"[{idx}] {usuario['nome']} - CPF: {usuario['cpf']}")
    usuario_idx = int(input("Selecione o número do usuário: "))
    if usuario_idx < 0 or usuario_idx >= len(usuarios):
        print("Usuário inválido.")
        return None
    return usuarios[usuario_idx]

# Função para listar todas as contas
def listar_contas(usuario: dict) -> dict:
    contas_usuario = [conta for conta in contas if conta['usuario'] == usuario]
    if not contas_usuario:
        print("Nenhuma conta cadastrada para este usuário.")
        return None
    print(f"Contas disponíveis para {usuario['nome']}:")
    for conta in contas_usuario:
        print(f"Conta {conta['numero_conta']} - Agência {conta['agencia']}")
    conta_numero = int(input("Selecione o número da conta: "))
    conta = next((c for c in contas_usuario if c['numero_conta'] == conta_numero), None)
    if not conta:
        print("Conta inválida.")
        return None
    return conta

# Função para listar todas as contas (de todos os usuários)
def listar_todas_contas() -> dict:
    if not contas:
        print("Nenhuma conta cadastrada.")
        return None
    print("Contas disponíveis:")
    for conta in contas:
        usuario = conta['usuario']
        print(f"Conta {conta['numero_conta']} - Agência {conta['agencia']} - Usuário: {usuario['nome']}")
    conta_numero = int(input("Selecione o número da conta: "))
    conta = next((c for c in contas if c['numero_conta'] == conta_numero), None)
    if not conta:
        print("Conta inválida.")
        return None
    return conta

# Simulação de uso
limite_saques = 3
limite_saque = 500.0

while True:
    print("""
    ** Banco PY **

    [1] Cadastrar Usuário
    [2] Cadastrar Conta
    [3] Depósito
    [4] Saque
    [5] Extrato
    [0] Sair
    """)
    operacao = input("Escolha uma opção: ")

    if operacao == "1":
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        cpf = input("CPF: ")
        endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        cadastrar_usuario(nome, data_nascimento, cpf, endereco)

    elif operacao == "2":
        cpf = input("Informe o CPF do usuário para vincular à conta: ")
        cadastrar_conta(cpf)

    elif operacao == "3":
        conta = listar_todas_contas()  # Lista todas as contas para seleção
        if conta:
            valor_depositado = float(input("Valor do depósito: "))
            if valor_depositado <= 0:
                print("Valor inválido.")
            else:
                conta['saldo'], conta['extrato'] = deposito(conta['saldo'], valor_depositado, conta['extrato'])
                print("Depósito realizado com sucesso.")
                exibir_extrato(conta['saldo'], extrato=conta['extrato'])

    elif operacao == "4":
        conta = listar_todas_contas()  # Lista todas as contas para seleção
        if conta:
            valor_sacado = float(input("Valor do saque: "))
            conta['saldo'], conta['extrato'] = saque(
                saldo_bancario=conta['saldo'],
                valor=valor_sacado,
                extrato=conta['extrato'],
                limite=limite_saque,
                numero_saques=conta['numero_saques'],
                limite_saques=limite_saques
            )
            if valor_sacado <= conta['saldo'] and conta['numero_saques'] < limite_saques and valor_sacado <= limite_saque:
                conta['numero_saques'] += 1
                print("Saque realizado com sucesso.")
                exibir_extrato(conta['saldo'], extrato=conta['extrato'])

    elif operacao == "5":
        conta = listar_todas_contas()  # Lista todas as contas para seleção
        if conta:
            exibir_extrato(conta['saldo'], extrato=conta['extrato'])

    elif operacao == "0":
        print("Saindo...")
        break

    input("Pressione ENTER para continuar...")
