import asyncio

'''
 CorOutines

    Coroutines are computer program components that generalize
    subroutines for non-preemptive multitasking, by allowing execution to be suspended and resumed
    (wikipedia)

    Ou seja, é um wrapper de funcão que permite executar as chamadas de forma assincrona
'''

'''
Aync Event Loop
In Computer  sicence, the event loop is a programming construct or design pattern
that waits for and dispatches events or messages in a program (Wikipedia)
'''

async def main():
    '''Retorno é uma coroutine'''
    print('Hello')
    await foo('TEXT')
    # Adicionando um novo print abaixo, o funcionamento seria semelhante a forma síncrona
    print("Vai esperar o await acima")


async def foo(text):
    print(text)
    await asyncio.sleep(1)

# A chamada abaixo retornaria um erro, pois, para executar uma coroutine é necessário um event loop
# main()

# Criando um event loop
asyncio.run(main())
