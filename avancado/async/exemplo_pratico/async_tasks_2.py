import asyncio
import time


async def coleta_banco_1():

    await asyncio.sleep(2)
    print("terminei de coletar do banco de dados!")
    return True

async def coleta_banco_2():

    await asyncio.sleep(2)
    print("Terminei de coletar do banco de dados!!")
    return True

async def coleta_endpoint():

    await asyncio.sleep(2)
    print("Terminei de coletar do banco de dados!!")
    return {"data": [{"coletado": "sucesso"}]}

async def executar_consultas():
    inicio = time.time()
    task1 = asyncio.create_task(coleta_banco_1())
    task2 = asyncio.create_task(coleta_banco_2())
    task3 = asyncio.create_task(coleta_endpoint())

    resutado1 = await task1
    resutado2 = await task2
    resutado3 = await task3

    print(resutado1)
    print(resutado2)
    print(resutado3)
    print(f"FIM: {time.time() - inicio}")

def main():
    asyncio.run(executar_consultas())

if __name__ == '__main__':
    main()