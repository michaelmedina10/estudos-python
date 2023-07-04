import requests
import os
import time

from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv('ALPHA_VANTAGE_KEY')

url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'IBM', 'VALE', 'PETR', 'BBAS', 'ITUB', 'HAPV', 'MGLU', 'PRIO3', 'GGBR']
results = []


def run_tasks():
    for symbol in symbols:
        response = requests.get(url.format(symbol, API_KEY))
        results.append(response.json())


print("Timer started...")
start = time.time()
run_tasks()
end = time.time()
total_time = end - start
print("Levou {} segundos para fazer {} chamadas sequenciais".format(total_time, len(symbols)))