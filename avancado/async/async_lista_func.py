import pandas as pd
import asyncio

async def consulta_banco_1():
    # código da consulta
    df = pd.DataFrame({'coluna1': [1, 2, 3], 'coluna2': ['a', 'b', 'c']})
    df['nome_funcao'] = 'func1'
    return df

async def consulta_banco_2():
    # código da consulta
    df = pd.DataFrame({'coluna3': [4, 5, 6], 'coluna4': ['d', 'e', 'f']})
    df['nome_funcao'] = 'func2'
    return df

async def consulta_banco_3():
    # código da consulta
    df = pd.DataFrame({'coluna5': [7, 8, 9], 'coluna6': ['g', 'h', 'i']})
    df['nome_funcao'] = 'func3'
    return df

async def executar_consultas_assincronas():
    tasks = [
        consulta_banco_1(),
        consulta_banco_2(),
        consulta_banco_3()
    ]
    df_list = await asyncio.gather(*[task for task in tasks])
    resultado = {}
    for df in df_list:
        nome_funcao = df['nome_funcao'][0]
        del df['nome_funcao']
        resultado[nome_funcao] = df
    return resultado

async def minha_funcao():
    # outras operações aqui
    resultados = await executar_consultas_assincronas()
    return resultados
    # processar os resultados aqui

# Chamada da função minha_funcao()
loop = asyncio.get_event_loop()
resultados = loop.run_until_complete(minha_funcao())
loop.close()

print(type(resultados))
print(resultados.keys())
print(resultados['func1'])
print(resultados['func2'])
print(resultados['func3'])