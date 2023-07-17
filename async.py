import asyncio

async def buscar_dados():
    print("Iniciando busca...")
    await asyncio.sleep(2)
    print("Busca Concluida!!!")
    return {"data": 1}


async def imprimir_numeros():
    for i in range(4):
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