class Veiculo:
    def __init__(self, marca, modelo, estado):
        self.marca = marca 
        self.modelo = modelo
        self._estado = False

    def __str__(self, marca, modelo, estado):
        return f'{marca} o {modelo} e  está {estado}'

print(Veiculo)