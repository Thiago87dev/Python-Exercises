nome = 'thiago alves'
contador = 0
novo_nome = ''
novo_nome2 = ''
while contador < len(nome):
    print(nome [contador])
    novo_nome += '*' + nome[contador] + '*'
    novo_nome2 += f'/{nome[contador]}'
    contador += 1

novo_nome = '*' + novo_nome + '*' # adicionando um * no inicio e outro no final
print(novo_nome)
novo_nome2 += '/' # adicionando uma / no final
print(novo_nome2)