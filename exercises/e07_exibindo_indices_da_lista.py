# nao fiz esse exercicio, apenas copiei e colei da aula

"""
Exercício
Exiba os índices da lista
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append(10)


indices = range(len(lista))

for i in indices:
    print(i, lista[i], type(lista[i]))