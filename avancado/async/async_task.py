import asyncio
import time

async def main():
    '''Retorno é uma coroutine'''
    print('Hello')
    # Create a task means "Python execute that function and while you do it, i'm going to continue with next statement"
    task = asyncio.create_task(foo('TEXT'))
    # if you want to wait, write await
    # await task

    '''
    quando a linha onde a task foi definida é chamada, o python diz:
    continue o fluxo da funcao atual até ela terminar, ou acontecer alguma quebra no fluxo, depois execute essa task.
    logo se eu colocar um sleep embaxio, o python irá considerar uma quebra de fluxo e executar a task e depois o vai esperar...
    '''
    await asyncio.sleep(1)
    # Adicionando um novo print abaixo, o funcionamento seria semelhante a forma síncrona
    print("Vai esperar o await acima")


async def foo(text):
    print(text)
    # O statement abaixo quebra o fluxo novamente, se for time.sleep() ele espera e continua nessa function
    await asyncio.sleep(10)
    # A quebra de fluxo acima, retorna para a principal, ignorando completamente o statement abaixo
    print("DEPOIS DO SEGUNDO SLEEP, SEGUNDA QUEBRA DE FLUXO")


# A chamada abaixo retornaria um erro, pois, para executar uma coroutine é necessário um event loop
# main()

# Criando um event loop
asyncio.run(main())