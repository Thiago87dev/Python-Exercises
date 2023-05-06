import re
import random

cpf = ''

for i in range(9):
    cpf += str(random.randint(0, 9))

sequencia = cpf == cpf[0] * len(cpf) # verificando se foram digitados numeros repitidos

contador = 0
soma = 0

if not sequencia:
    for i in range(10, 1, -1):
        soma += i * int(cpf[contador])
        contador += 1

    primeiro_digito = (soma * 10) % 11

    if primeiro_digito > 9:
        primeiro_digito = 0

    cpf += str(primeiro_digito)
    soma = 0
    contador = 0
    
    for i in range(11, 1, -1):
        soma += i * int(cpf[contador])
        contador += 1

    segundo_digito = (soma * 10) % 11

    if segundo_digito > 9:
        segundo_digito = 0

    cpf += str(segundo_digito)
    cpf = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:11])
    print(cpf)
    