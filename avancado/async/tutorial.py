import asyncio

async def buscar_dados():
    print("Iniciando busca...")
    await asyncio.sleep(2)
    print("Busca Concluida!!!")
    return {"data": 1}


async def imprimir_numeros():
    for i in range(5):
        print(i)
        await asyncio.sleep(1)


async def executar_tasks():
    task1 = asyncio.create_task(buscar_dados())
    task2 = asyncio.create_task(imprimir_numeros())

    value = await task1
    print(value)
    await task2

def principal():
    asyncio.run(executar_tasks())

if __name__ == '__main__':
    principal()

'''
fica claro que a primeira task vai levar 2 segundos para executar, enquanto na segunda cada iteracao leva 0.25 seg,
logo, 2 / 0.25 = 8, ou seja vou conseguir printar 8 numeros ate o 'request' esta finalizado e eu ter um response pronto.
Outro ponto importante é que eu tenho de mandar esperar , pois, caso contrário, iremos retornar uma Future (promisse do JavaScript), indica
que no futuro pode haver um resultado naquela variavel, mais ainda nao tem.
'''

'''
Caso eu nao use o Await, o event loop ira fazer o schedule das tasks, executar todos statements e acabar, ele nao vai esperar
o termino das tasks
'''
# print(task1)