import json
# criar arquivo para apagar

def gerar_arquivo_temp():
    with open('modulos_python/arquivo_tmp.txt', 'w') as f:
        json.dump('vou apagar vc', f)

# od.shutil - Mover, copiar e apagar arquivos
# mover/renomear -> Shutil.move
# mover/renomear -> os.rename
# copiar -> shutil.copy
# apagar -> os.unlink
# apagar diretório recurvisamente -> os.rmtree

import os
import shutil

# criar pasta para mover arquivo
diretorio = os.path.dirname(__file__)
caminho_para_pasta_nova = os.path.join(diretorio, 'nova_pasta_para_mover_arquivos')

# cria pasta
os.makedirs(caminho_para_pasta_nova, exist_ok=True)

# gera dentro da pasta modulos_python
gerar_arquivo_temp()
# move para a pasta nova_pasta_para_mover_arquivos

shutil.move(os.path.join(diretorio, 'arquivo_tmp.txt') , caminho_para_pasta_nova)

# copia um arquivo para outro lugar
# shutil.copy(os.path.join(os.getcwd(), 'modulos_python/arquivo_tmp.txt' ), caminho_para_pasta_nova)


