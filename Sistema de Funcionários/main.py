from empresa import Empresa
from funcionario_assalariado import FuncionarioAssalariado
from funcionario_horista import FuncionarioHorista
from funcionario_comissionado import FuncionarioComissionado


empresa = Empresa("Tech Solutions")

f1 = FuncionarioAssalariado("Carlos", "111.111.111-11", 5000)
f2 = FuncionarioHorista("Ana", "222.222.222-22", 160, 35)
f3 = FuncionarioComissionado("Pedro", "333.333.333-33", 20000, 0.10)

empresa.adicionar_funcionario(f1)
empresa.adicionar_funcionario(f2)
empresa.adicionar_funcionario(f3)

empresa.listar_funcionarios()
empresa.mostrar_folha_pagamento()
