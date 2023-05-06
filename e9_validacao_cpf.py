import re

cpf = input('digite seu cpf ')

cpf = cpf.strip() # tirando os espaços

sequencia = cpf == cpf[0] * len(cpf) # verificando se foram digitados numeros repitidos

padra_cpf_sem_pontos = r'^\d{11}$' # padrao para cpf apenas com numeros

if re.match(padra_cpf_sem_pontos, cpf): # verificando se foi digitado cpf apenas com numeros
    cpf = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:]) # caso sim, adicionando caracteres

cpf_para_conferir = cpf.replace('.', '').replace('-', '') 
contador = 0
soma = 0

padrao_cpf = r'^\d{3}.\d{3}.\d{3}-\d{2}$'

if re.match(padrao_cpf, cpf) and not sequencia:
    cpf_formatado = cpf[:-3].replace('.', '') # excluindo os 3 ultimos digitos (poderia ser pegando os 9 primeiro [:9] ) e tirando 
    # os pontos

    for i in range(10, 1, -1):
        soma += i * int(cpf_formatado[contador])
        contador += 1

    primeiro_digito = (soma * 10) % 11

    if primeiro_digito > 9:
        primeiro_digito = 0

    print(primeiro_digito)

    cpf_formatado = cpf_formatado + str(primeiro_digito)
    soma = 0
    contador = 0
    
    for i in range(11, 1, -1):
        soma += i * int(cpf_formatado[contador])
        contador += 1

    segundo_digito = (soma * 10) % 11

    if segundo_digito > 9:
        segundo_digito = 0

    print(segundo_digito)

    cpf_formatado = cpf_formatado + str(segundo_digito)
    print(cpf_para_conferir)
    print(cpf_formatado)

    if cpf_para_conferir == cpf_formatado:
        print(f'o cpf {cpf} é VALIDO')
    else:
        print(f'o cpf {cpf} é INVALIDO')

else:
    print('Formato do cpf incorreto')