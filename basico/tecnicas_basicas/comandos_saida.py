
# Comentario basico do python, ignorado pelo interpretador

# Comando de saida python
print("Hello World")

nome = "Michael"
idade = 26

# Comando Formatando String de acordo com variáveis
print(f"Nome: {nome}; Idade: {idade}")
print("Nome: %s; Idade: %d" % (nome, idade))
print("Nome: " + nome + "; " + "Idade: " + str(idade))

# Argumentos nao nomeados com sep
print(10, 24)
print(10, 24, sep='-')
print(10, 24, sep='teste', end="SEMEND")
print("NAO ESTA NA Linha DE BAIXO")

# Python é case sensitive
# Print() não existe é print()
