"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('digite um numero inteiro ')
try:
    if int(numero) % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é impar')
except:
    print('digite um numero inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('digite a hora ')
hora_int = int(hora)
if hora_int >= 0 and hora_int <= 11:
    print('bom dia')
elif hora_int >= 12 and hora_int <= 17:
    print('boa tarde')
elif hora_int >= 18 and hora_int <= 23:
    print('boa noite')
else:
    print('hora invalida')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('digite seu nome ')

if len(nome) <= 4:
    print('seu nome é curto')
elif len(nome) == 5 or len(nome) == 6:
    print('seu nome é normal')
else:
    print('seu nome é grande')