import tkinter as tk
from sistema import criar_conta, listar_contas

def menu():

    janela = tk.Tk()
    janela.title("Sistema Bancário")
    janela.geometry("800x800")

    # CAMPOS
    label_nome = tk.Label(janela, text="Nome")
    label_nome.pack()

    entrada_nome = tk.Entry(janela)
    entrada_nome.pack()

    label_saldo = tk.Label(janela, text="Saldo Inicial")
    label_saldo.pack()

    entrada_saldo = tk.Entry(janela)
    entrada_saldo.pack()

    # LISTA DE CONTAS
    lista = tk.Listbox(janela)
    lista.pack(pady=10)

    # FUNÇÕES

    def atualizar_lista():

        lista.delete(0, tk.END)

        for i, conta in enumerate(listar_contas()):
            lista.insert(tk.END, f"{i} - {conta.titular}")

    def criar():

        nome = entrada_nome.get()
        saldo = float(entrada_saldo.get())

        criar_conta(nome, saldo)

        atualizar_lista()

    def acessar():

        indice = lista.curselection()[0]
        conta = listar_contas()[indice]

        abrir_conta(conta)

    # BOTÕES

    botao_criar = tk.Button(janela, text="Criar Conta", command=criar)
    botao_criar.pack(pady=5)

    botao_listar = tk.Button(janela, text="Atualizar Lista", command=atualizar_lista)
    botao_listar.pack(pady=5)

    botao_acessar = tk.Button(janela, text="Acessar Conta", command=acessar)
    botao_acessar.pack(pady=5)

    janela.mainloop()


def abrir_conta(conta):

    janela = tk.Toplevel()
    janela.title(f"Conta - {conta.titular}")
    janela.geometry("300x300")

    label_saldo = tk.Label(janela, text="Saldo: ")
    label_saldo.pack(pady=10)

    entrada_valor = tk.Entry(janela)
    entrada_valor.pack()

    def atualizar():
        label_saldo.config(text=f"Saldo: {conta.ver_saldo()}")

    def depositar():

        valor = float(entrada_valor.get())
        conta.depositar(valor)

        atualizar()

    def sacar():

        valor = float(entrada_valor.get())
        conta.sacar(valor)

        atualizar()

    botao_saldo = tk.Button(janela, text="Ver Saldo", command=atualizar)
    botao_saldo.pack(pady=5)

    botao_depositar = tk.Button(janela, text="Depositar", command=depositar)
    botao_depositar.pack(pady=5)

    botao_sacar = tk.Button(janela, text="Sacar", command=sacar)
    botao_sacar.pack(pady=5)