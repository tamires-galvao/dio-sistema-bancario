---

# Sistema Bancário em Python

Este projeto implementa um sistema bancário simples em Python, que permite realizar operações como **depósitos**, **saques** e exibir o **extrato**. O sistema é controlado por um menu interativo em linha de comando.

## Funcionalidades

- **Depositar**: Permite adicionar fundos à conta, registrando o valor no extrato.
- **Sacar**: Permite retirar fundos da conta, com as seguintes regras:
  - Limite de **R$ 500,00 por saque**.
  - Limite de **3 saques diários**.
  - O saldo deve ser suficiente para realizar o saque.
- **Exibir Extrato**: Mostra todas as transações realizadas e o saldo atual.
- **Sair**: Encerra o programa.

## Regras

- O sistema limita o valor de saque a **R$ 500,00** por transação.
- O número máximo de saques por dia é **3**.
- Não é permitido sacar um valor superior ao saldo disponível.

## Tecnologias Utilizadas

- **Linguagem**: Python 3.x

## Como Executar

1. **Clone o repositório**:
   ```bash
   git clone git@github.com:tamires-galvao/dio-sistema-bancario.git
   ```

2. **Navegue até o diretório do projeto**:
   ```bash
   cd dio-sistema-bancario
   ```

3. **Execute o script Python**:
   ```bash
   python sistema_bancario.py
   ```

4. **Interaja com o menu** que será exibido no terminal, escolhendo as opções para depositar, sacar, exibir o extrato ou sair do sistema.

## Exemplo de Uso

```text
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> d
Informe o valor do depósito: 100
Depósito de R$ 100.00 realizado com sucesso!

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> s
Informe o valor do saque: 50
Saque de R$ 50.00 realizado com sucesso!

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> e

================ EXTRATO ================
Depósito: R$ 100.00
Saque: R$ 50.00

Saldo atual: R$ 50.00
=========================================
```
---
