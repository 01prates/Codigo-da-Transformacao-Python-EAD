class carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

    meu_carro = Carro("ferrari", "f40")
    print(meu_carro.exibir_info())

