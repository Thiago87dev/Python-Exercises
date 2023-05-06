# def par_impar(num):
#     resultado = ''
#     if num % 2 == 0:
#         resultado = 'par'
#     else:
#         resultado = 'impar'
#     return resultado

# par_ou_impar = par_impar(1)
# print(par_ou_impar)

def par_impar(num):
    par = num % 2 == 0
    if par:
        return f'{num} é par'
    return f'{num} é impar'

print(par_impar(7))