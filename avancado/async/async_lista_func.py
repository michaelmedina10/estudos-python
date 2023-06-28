import pandas as pd
import asyncio

async def consulta_banco_1():
    # código da consulta
    df = pd.DataFrame({'coluna1': [1, 2, 3], 'coluna2': ['a', 'b', 'c']})
    df['nome_funcao'] = 'func1'
    return df

async def consulta_banco_2():
    # código da consulta
    df = pd.DataFrame({'coluna1': [4, 5, 6], 'coluna2': ['d', 'e', 'f']})
    df['nome_funcao'] = 'func2'
    return df

async def consulta_banco_3():
    # código da consulta
    df = pd.DataFrame({'coluna1': [7, 8, 9], 'coluna2': ['g', 'h', 'i']})
    df['nome_funcao'] = 'func3'
    return df

async def executar_consultas_assincronas():
    tasks = [consulta_banco_1(), consulta_banco_2(), consulta_banco_3()]
    df_list = await asyncio.gather(*[task for task in tasks])
    return df_list

async def minha_funcao():
    # outras operações aqui
    resultados = await executar_consultas_assincronas()
    return resultados
    # processar os resultados aqui

# Chamada da função minha_funcao()
resultados = asyncio.run(minha_funcao())
print(pd.concat([df for df in resultados], ignore_index=True))