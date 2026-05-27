from armazenador_arquivo import ArmazenadorArquivo
from armazenador_banco import ArmazenadorBanco
from armazenador_nuvem import ArmazenadorNuvem
from funcoes import (
    executar_salvamento_formal,
    executar_salvamento_flexivel
)


arquivo = ArmazenadorArquivo()
banco = ArmazenadorBanco()
nuvem = ArmazenadorNuvem()

executar_salvamento_formal(arquivo, "dados.txt")
executar_salvamento_formal(banco, "clientes")

executar_salvamento_flexivel(arquivo, "backup.txt")
executar_salvamento_flexivel(nuvem, "foto.png")
