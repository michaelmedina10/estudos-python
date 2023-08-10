# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()

# Para timezones temos o módulo pytz
# pip3 install pytz types-pytz

from datetime import datetime, timedelta
from pytz import timezone

data = datetime(2022, 7, 10)
print(data)

# mapear uma data em formato string para data like
data_str = '2022-04-10 08:25:10'
data_str_fmt = '%Y-%m-%d %H:%M:%S'
data = datetime.strptime(data_str, data_str_fmt)
print(data)

print("*" * 100)
# formatar data object para um formato string
data_str_fmt = '%d/%m/%Y %H:%M:%S'
data = datetime.strftime(data, data_str_fmt)
print(data)
print(type(data))

print("*" * 100)
# datetime.now()
print(datetime.now())

# datetime com timezone
print("*" * 100)
print(datetime.now(tz=timezone(zone='Asia/Tokyo')))


# diferenca entre datas
print("*" * 100)
data_str_fmt = '%Y-%m-%d %H:%M:%S'
data_fim = datetime.strptime('2022-04-10 08:25:10', data_str_fmt)
data_inicio = datetime.strptime('1987-04-10 08:25:10', data_str_fmt)
delta = data_fim - data_inicio
print(delta)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())

print("*" * 100)
# acrescentando ou subtraindo unidades de tempo
data_str_fmt = '%Y-%m-%d'
delta = timedelta(days=10, hours=2)  # acrescendo 10 dias e 2 horas
print(datetime.strptime('2022-04-10', data_str_fmt) + delta)

