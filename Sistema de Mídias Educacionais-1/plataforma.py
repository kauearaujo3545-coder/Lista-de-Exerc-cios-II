class Plataforma:
    def __init__(self, nome):
        self.nome = nome
        self.midias = []

    def adicionar_midia(self, midia):
        self.midias.append(midia)

    def listar_midias(self):
        print(f"\nMídias da plataforma {self.nome}:")
        for midia in self.midias:
            midia.mostrar_info()
            print("-" * 30)

    def reproduzir_todas(self):
        print("\nReproduzindo todas as mídias:")
        for midia in self.midias:
            midia.reproduzir()
