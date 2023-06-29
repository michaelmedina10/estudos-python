# Desempacotamento e empacotamento de dicionarios

pessoas = {
    "nome": "Fulano",
    "sobrenome": "Siclano"
}

#chaves
chave1, chave2 = pessoas
print(chave1, chave2)

#values
value1, value2 = pessoas.values()
print(value1, value2)

# tupla chave, valor
item1, item2 = pessoas.items()
print(item1, item2)

# desempacotar os itens
(a1,a2), (b1, b2) = pessoas.items()
print(a1, a2)
print(b1, b2)

# desempacotar dicionarios dentro de outros
dados_pessoa = {
    "idade": 16,
    "altura": 1.75,
    "hobbies": ["ler", "video game"]
}

# spread é uma cópia por valor e não por referência, inclusive com deepcopy
dados_pessoa_completa = {**pessoas, **dados_pessoa}
dados_pessoa_completa["hobbies"] = "ALTEREI HOBBIES"
print(dados_pessoa_completa)
print(dados_pessoa)

# KWargs em funções
def mostro_dados_nomeados(**kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

# Caso eu não passe os argumentos nomeados, no caso com o nome e sobrenome ele entraria como args
mostro_dados_nomeados(nome="Michael", sobrenome="Medina")

# caso eu ja tenha um dicionario e queira desempacotar nos argumentos, eu posso
mostro_dados_nomeados(**dados_pessoa_completa)
