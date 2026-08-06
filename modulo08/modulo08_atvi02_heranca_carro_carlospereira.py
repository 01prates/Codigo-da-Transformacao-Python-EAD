class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

    meu_carro = Carro("ferrari", "f40")
    print(meu_carro.exibir_info())

class Carro_Elétrico(Carro):
    def __init__(self, marca, modelo, ano, autonomia_bateria):
        super().__init__(marca, modelo, ano)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        info_base = super().exibir_info()
        return f"{info_base},| Autonomia da bateria: {self.autonomia_bateria} km"
    meu_carro_eletrico = Carro_Elétrico("tesla", "model s", 2022, 600)
    print(meu_carro_eletrico.exibir_info())