perguntas = [
    {
        'pergunta': 'quanto é 2+2 ?',
        'options': ['3','4','5','6'],
        'resposta': '4',
    },
    {
        'pergunta': 'quanto é 3+3 ?',
        'options': ['3','4','5','6'],
        'resposta': '6',
    },
    {
        'pergunta': 'quanto é 1+2 ?',
        'options': ['3','4','5','6'],
        'resposta': '3',
    },
]

qnt_acertou = 0
for i in perguntas:
    print()
    print(i['pergunta'])
    print()

    options = i['options']
    for index, j in enumerate(options) :
        print(f'{index+1}) {j}')
    print()

    escolha = input('escolha uma opção ')

    acertou = False
    escolha_int = None

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < len(options) + 1:
            if options[escolha_int-1] == i['resposta']:
                acertou = True
                qnt_acertou += 1
      
    if acertou:
        print('acertou')
    else:
        print('errou')
        
print()
print(f'vc acertou {qnt_acertou} de {len(perguntas)} perguntas')
print()
       
       