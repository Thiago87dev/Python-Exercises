# do jeito que o professor fez

class Carro:
    def __init__(self, nome, motor, fabricante):
        self.nome = nome
        self.motor = motor
        self.fabricante = fabricante

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

motor_1_0 = Motor('1.0')
motor_1_6 = Motor('1.6')
motor_2_0 = Motor('2.0')

ford = Fabricante('ford')
renault = Fabricante('renault')
fiat = Fabricante('fiat')

ka = Carro('ka', motor_1_0, ford)
fiesta = Carro('fiesta', motor_1_6, ford)
clio = Carro('clio', motor_1_0, renault)
logan = Carro('logan', motor_1_0, renault)
sandero = Carro('sandero', motor_1_6, renault)
uno = Carro('uno', motor_1_0, fiat)
palio = Carro('palio', motor_1_0, fiat)


print(ka.fabricante.nome, ka.nome, ka.motor.nome)
print(fiesta.fabricante.nome, fiesta.nome, fiesta.motor.nome)
print(clio.fabricante.nome, clio.nome, clio.motor.nome)
print(logan.fabricante.nome, logan.nome, logan.motor.nome)
print(sandero.fabricante.nome, sandero.nome, sandero.motor.nome)
print(uno.fabricante.nome, uno.nome, uno.motor.nome)
print(palio.fabricante.nome, palio.nome, palio.motor.nome)