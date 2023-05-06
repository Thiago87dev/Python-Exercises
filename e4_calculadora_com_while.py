while True:
    num1 = input('digite um numero ')
    operador = input('digite um operador ')
    num2 = input('digite outro numero ')
    
    try:

        if operador == '/':
            if num2 == '0':
                print('não é possivel dividir por 0')
                continue
            resultado = float(num1) / float(num2)
        elif operador == '*':
            resultado = float(num1) * float(num2)
        elif operador == '+':
            resultado = float(num1) + float(num2)
        elif operador == '-':
            resultado = float(num1) - float(num2)
        else:
            print('digite um operador valido')
            continue
    except:
        print('digite numeros validos')
        continue

    print(f'o resultado de {num1} {operador} {num2} é {resultado}')

    sair = input('Quer sair? [s]im ').lower().startswith('s')
    

    if sair is True:
        break