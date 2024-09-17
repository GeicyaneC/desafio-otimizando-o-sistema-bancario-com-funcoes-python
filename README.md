
# DESAFIO 2 | OTIMIZANDO O SISTEMA BANCÁRIO COM FUNÇÕES PYTHON

Este é um projeto simples de um sistema bancário criado em Python, permitindo operações como cadastro de usuários, criação de contas bancárias, depósitos, saques e consulta de extratos. O objetivo deste sistema é simular operações bancárias de maneira fácil, com foco em aprender e praticar conceitos de funções, manipulação de listas e tratamento de dados.

## 🔧 FUNCIONALIDADES

- Cadastro de Usuários
- Cadastro de contas
- Depósitos
- Saques
- Extratos

## 💻REQUISITOS

Este projeto é um script Python simples, sem dependências externas, exceto o Python 3.x.

## Estrutura de Código


```
- cadastrar_usuario(nome, data_nascimento, cpf, endereco): Cadastra um novo usuário.
- cadastrar_conta(cpf): Cria uma conta vinculada a um usuário através do CPF.
- deposito(saldo_bancario, valor, extrato): Realiza depósito em uma conta.
- saque(saldo_bancario, valor, extrato, limite, numero_saques, limite_saques): Realiza saque de uma conta, obedecendo os limites de valor e quantidade de saques.
- exibir_extrato(saldo, extrato): Exibe o saldo e o extrato de transações de uma conta.
- listar_usuarios(): Lista todos os usuários cadastrados.
- listar_contas(usuario): Lista todas as contas de um determinado usuário.
- listar_todas_contas(): Lista todas as contas cadastradas no sistema.

```

## Contribuições
Sinta-se à vontade para sugerir melhorias ou correções. Você pode abrir uma issue ou fazer um pull request neste repositório.
