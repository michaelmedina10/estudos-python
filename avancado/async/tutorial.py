import asyncio

async def fetch_data():
    print("Start fetching")
    await asyncio.sleep(2)
    print("done fetching")
    return {"data": 1}


async def print_numbers():
    for i in range(5):
        print(i)
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = await task1
    print(value)
    await task2


asyncio.run(main())

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