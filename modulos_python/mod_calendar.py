# Calendar é usado para coisas genéricas de calendários e datas
# com calendar, podemos saber:
#   - Qual o último dia do mês (ex. monthrange).
#   - Qual o nome e número do dia de determinada hora (ex. weekday).
#   - Criar um calendário em si (ex. monthcalendar).
# Trabalhar com coisas especificas de calendario como (Calendários, meses etc).
# o dias são representados de 0 a 6

import calendar

print(calendar.calendar(2023))
print(calendar.month(2023, 7))
print(list(calendar.month_name))

print("*" * 100)
# último dia do mês
numero_dia_primeiro, ultimo_dia = calendar.monthrange(2023, 8)
print(numero_dia_primeiro, ultimo_dia)
print(calendar.day_name[numero_dia_primeiro])
print(calendar.day_name[calendar.weekday(2023, 8, ultimo_dia)])


print("*" * 100)

lista_days_and_numbers = []
for week in calendar.monthcalendar(2023, 8):
    for day, day_number in list(enumerate(week)):
        lista_days_and_numbers.append((calendar.day_name[day], day_number))

print(lista_days_and_numbers)