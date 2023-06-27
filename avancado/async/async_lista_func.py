import pandas as pd
import asyncio

'''
Entendi, no seu exemplo as funções A, B e C são chamadas dentro da função executar_consultas_assincronas
através da função asyncio.gather. Nesse caso, a palavra-chave await não é necessária nas funções individuais
porque o objeto retornado por asyncio.gather já espera os resultados de todas as corrotinas passadas como argumento.

Ao usar asyncio.gather, você está criando uma tarefa que contém várias corrotinas, e essa tarefa
será executada em paralelo utilizando o loop de eventos do asyncio. Assim, o loop de eventos
irá esperar o término de todas as corrotinas incluídas na tarefa antes de continuar com a execução do programa.

Dessa forma, quando a função executar_consultas_assincronas chama asyncio.gather(consulta_banco_1(), consulta_banco_2(), consulta_banco_3()), ela
cria uma tarefa que contém as três corrotinas e aguarda até que
todas essas corrotinas sejam concluídas antes de retornar um valor para a variável df_list.
Portanto, nesse caso, a palavra-chave await não é necessária nas funções individuais.
'''

async def consulta_banco_1():
    # código da consulta
    return pd.DataFrame({'coluna1': [1, 2, 3], 'coluna2': ['a', 'b', 'c']})

async def consulta_banco_2():
    # código da consulta
    return pd.DataFrame({'coluna3': [4, 5, 6], 'coluna4': ['d', 'e', 'f']})

async def consulta_banco_3():
    # código da consulta
    return pd.DataFrame({'coluna5': [7, 8, 9], 'coluna6': ['g', 'h', 'i']})

async def executar_consultas_assincronas():
    tasks = [consulta_banco_1(), consulta_banco_2(),consulta_banco_3()]
    df_list = await asyncio.gather(*tasks)
    return df_list

if __name__ == '__main__':
    resultado = asyncio.run(executar_consultas_assincronas())
    print(len(resultado))
    print(resultado[0])
    print(resultado[1])
    print(resultado[2])
    print(type(resultado[0]))