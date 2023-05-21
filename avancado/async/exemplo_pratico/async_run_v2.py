import asyncio
import aiohttp
import os
import time
# To work with the .env file
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('ALPHA_VANTAGE_KEY')
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'IBM', 'IBM', 'VALE', 'PETR', 'BBAS', 'ITUB', 'HAPV', 'MGLU', 'PRIO3', 'GGBR']
results = []

start = time.time()

async def get_symbols():
    async with aiohttp.ClientSession() as session:
        tasks = [session.get(url.format(symbol, API_KEY), ssl=False) for symbol in symbols]
        # Criando uma lista de tasks, usando o gather, para indicar que queremos fazer todos os requests ao msm tempo
        # e só continuar a execucao quando todas tasks forem finalizadas
        responses = await asyncio.gather(*tasks)
        [results.append(await response.json()) for response in responses]

asyncio.run(get_symbols())

end = time.time()
total_time = end - start
print("It took {} seconds to make {} API calls".format(total_time, len(symbols)))
print('You did it!')