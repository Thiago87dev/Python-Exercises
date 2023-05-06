# do jeito que eu fiz

class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []

    def fabricar_carro(self, motor, nome):
        self.carros.append(Carro(motor, nome))

    def exibir_carros(self):
        print(self.nome)
        for i in self.carros:
            print(i.nome, i.motor.nome)
        print()

class Carro:
    def __init__(self, motor, nome):
        self.nome = nome
        self.motor= motor

class Motor:
    def __init__(self, nome):
        self.nome = nome

fabricante1 = Fabricante('Renault')
fabricante2 = Fabricante('ford')

motor1 = Motor('motor123')
motor2 = Motor('motor777')
motor3 = Motor('motor001')

fabricante1.fabricar_carro(motor1, 'clio')
fabricante1.fabricar_carro(motor1, 'sandero')
fabricante1.fabricar_carro(motor2, 'logan')
fabricante2.fabricar_carro(motor3, 'fiesta')
fabricante2.fabricar_carro(motor3, 'ka')

fabricante1.exibir_carros()
fabricante2.exibir_carros()
