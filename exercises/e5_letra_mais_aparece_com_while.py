# descobrindo qual letra apareceu mais vezes no texto abaixo usando while

texto = 'Eu estou digitando um texto qualquer, só para saber qual letra aparece mais vezes. Isso é um teste.'
texto_editado = texto.lower().replace(' ', '')
i = 0
qnt_letra = 0
maior_qnt_letra = 0
letra_que_mais_aparece = ''

while i < len(texto_editado):
   
    qnt_letra = texto_editado.count(texto_editado[i])

    if qnt_letra > maior_qnt_letra:
        letra_que_mais_aparece = texto_editado[i]
        maior_qnt_letra = qnt_letra

    print(texto_editado[i], qnt_letra)
    i += 1
print(f'a letra que mais aparece é: "{letra_que_mais_aparece}", ela aparece {maior_qnt_letra} vezes')