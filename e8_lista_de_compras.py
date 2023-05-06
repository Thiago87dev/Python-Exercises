lista_compras = ['margarina', 'sabão em pó']

while True:
    codigo = input('digite 1 para ver a lista\ndigite 2 para adicionar um item a lista\ndigite 3 para apagar um item de uma lista\n\
digite "sair" a qlq momento para sair do programa ')
    codigo = codigo.lower()
    if codigo == 'sair':
        break
    try:

        codigo = int(codigo)
        if codigo == 1:
            print()
            for i, j in enumerate(lista_compras):
                print(i, j)
            print()
        elif codigo == 2:
            print()
            produto = input('digite o nome do produto ')
            produto = produto.lower()
            if produto == 'sair':
                break
            lista_compras.append(produto)
            for i, j in enumerate(lista_compras):
                print(i, j)
            print()
        elif codigo == 3:
            try:
                print()
                for i, j in enumerate(lista_compras):
                    print(i, j)
                apagar = input('\ndigite o indice a ser apagado ')
                apagar = apagar.lower()
                if apagar == 'sair':
                    break
                apagar = int(apagar)
                lista_compras.pop(apagar)
                for i, j in enumerate(lista_compras):
                    print(i, j)
                print()
            except:
                print('\neste indice não existe\n')
        else:
            print('\nescolha um numero valido ou digite "sair" para sair seu burro\n')
    except:
            print('\ndigite só numeros seu burro, ou escreva "sair" para sair\n')