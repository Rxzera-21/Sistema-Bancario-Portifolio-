from contas import Conta

contas = []

def criar_conta(nome, saldo):
    conta = Conta(nome, saldo)
    contas.append(conta)

def listar_contas():
    return contas