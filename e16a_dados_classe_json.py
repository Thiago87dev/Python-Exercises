# salvando os dados de uma instacia de classe em um arquivo json

import json

caminho_arquivo = "pessoa.json"

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Thiago', 25)
p2 = Pessoa('joao', 27)
p3 = Pessoa('maria', 32)

dados = [vars(p1), vars(p2), vars(p3)]

def fazer_dump():
    print('fazendo dump')
    #abre um arquivo e escrebe a str json nele
    with open(caminho_arquivo, "w") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)

if __name__=='__main__':
    fazer_dump()