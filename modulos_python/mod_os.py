import os

caminho = os.path.join('Documents', 'caminho', 'arquivo.txt')
print(caminho)

diretorio, arquivo = os.path.split(caminho)
print(diretorio, arquivo)

arquivo, extensao = os.path.splitext(arquivo)
print(arquivo, extensao)

# posso verificar lista de diretorios com:
# - os.path.listdir(caminho)

# posso verificar se o camino é um diretorio realmente:
# - os.path.isdir(caminho)