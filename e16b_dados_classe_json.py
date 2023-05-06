# criando uma instancia de uma classe usando o arquivo json salvo anteriormente

from e16a_dados_classe_json import caminho_arquivo, Pessoa
import json

# abre o arquivo json contendo os dados
with open(caminho_arquivo, "r") as arquivo:
    dados_json = json.load(arquivo)

p1 = Pessoa(**dados_json[0])
p2 = Pessoa(**dados_json[1])
p3 = Pessoa(**dados_json[2])

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)