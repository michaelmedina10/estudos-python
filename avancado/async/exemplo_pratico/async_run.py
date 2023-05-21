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
        for symbol in symbols:
            print('Working on symbol {}'.format(symbol))
            response = await session.get(url.format(symbol, API_KEY), ssl=False)
            results.append(await response.json())

asyncio.run(get_symbols())
# comando acima é a msm coisa das linhas abaixo
# loop = asyncio.get_event_loop()
# loop.run_until_complete(get_symbols())
# loop.close()
end = time.time()
total_time = end - start
print("It took {} seconds to make {} API calls".format(total_time, len(symbols)))
print('You did it!')