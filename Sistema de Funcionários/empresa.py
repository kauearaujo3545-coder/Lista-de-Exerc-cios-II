class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"\nFuncionários da empresa {self.nome}:")
        for funcionario in self.funcionarios:
            funcionario.mostrar_dados()
            print("-" * 30)

    def mostrar_folha_pagamento(self):
        print("\nFolha de pagamento:")
        for funcionario in self.funcionarios:
            pagamento = funcionario.calcular_pagamento()
            print(f"{funcionario.nome}: R$ {pagamento:.2f}")
