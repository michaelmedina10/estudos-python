import asyncio
import aiohttp
import requests
import os
import time
import warnings
from dotenv import load_dotenv
warnings.filterwarnings('ignore')
load_dotenv()

API_KEY = os.getenv('ALPHA_VANTAGE_KEY')
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'IBM', 'IBM', 'VALE', 'PETR', 'BBAS', 'ITUB', 'HAPV', 'MGLU', 'PRIO3', 'GGBR']
results = []


async def fazer_request(url):
    session = requests.Session()
    session.verify = False
    respose = await asyncio.get_event_loop().run_in_executor(None, session.get, url)
    return respose.json()


async def agregador_requisicao():
    dados = await asyncio.gather(*[fazer_request(url.format(symbol, API_KEY)) for symbol in symbols])
    return dados


inicio = time.time()
dados = asyncio.run(agregador_requisicao())
fim = time.time() - inicio

print(f"Tempo de Execução: {fim}")