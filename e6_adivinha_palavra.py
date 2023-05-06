import os
import random

palavras = ['espanha', 'estupido', 'espelho', 'estrago', 'esquece', 'esgoto', 'escroto','estranho', 'esporte', 'escravo',
'estrume', 'estrece']
palavra = random.choice(palavras)
erro = 0
letras_acertadas = ''
letras_erradas = ''

print('bem vindo ao jogo de adivinhação')
print('digite sair a qlq momento para sair')

while True:
    resultado = '' 
    
    letra = input('digite uma letra ' )
    if letra == 'sair':
        break
    
    if letra in letras_acertadas or letra in letras_erradas:
        print('vc ja digitou essa letra')
        erro += 1
        continue

    if letra in palavra:
        letras_acertadas += letra
        print('vc acertou')
    else:
        print('vc errou')
        erro += 1
        letras_erradas += letra
    
    for i in palavra:
        if i in letras_acertadas:
            resultado += i
        else:
            resultado += '*'
    print(f'{resultado}\n' )

    if resultado == palavra:
        os.system('cls')
        print(f'vc ganhou. a palavra é: {palavra}, vc errou {erro}x')
        palavra = random.choice(palavras)
        resultado = ''
        erro = 0
        letras_acertadas = ''
        letras_erradas = ''
        
        