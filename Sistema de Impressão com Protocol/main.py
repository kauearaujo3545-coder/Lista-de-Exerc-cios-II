from boleto import Boleto
from etiqueta import Etiqueta
from relatorio_simples import RelatorioSimples
from processador import processar_impressao


boleto = Boleto("123456", 250.75)
etiqueta = Etiqueta("Maria", "Rua A, 123")
relatorio = RelatorioSimples("Relatório Financeiro")

processar_impressao(boleto)
processar_impressao(etiqueta)
processar_impressao(relatorio)
