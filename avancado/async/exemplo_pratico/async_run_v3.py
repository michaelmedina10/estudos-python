import asyncio
import aiohttp
import os
import time

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('ALPHA_VANTAGE_KEY')

endpoint = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
# 13 chamadas
lista_acoes = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'IBM', 'VALE', 'PETR', 'BBAS', 'ITUB', 'HAPV', 'MGLU', 'PRIO3', 'GGBR']
results = []

async def fazer_requisicao():
    async with aiohttp.ClientSession() as session:
        tasks = [session.get(endpoint.format(acoes, API_KEY), ssl=False) for acoes in lista_acoes]

        responses = await asyncio.gather(*tasks)
        [results.append(await response.json()) for response in responses]

# Asyncio.run() inicia o event loop somente, logo ele pode ser invocado dentro de uma função síncrona
def main():
    inicio = time.time()
    asyncio.run(fazer_requisicao())
    fim = time.time()
    tempo_execucao = fim - inicio
    print("Levou {} segundos para fazer {} chamadas".format(tempo_execucao, len(lista_acoes)))

if __name__ == '__main__':
    main()