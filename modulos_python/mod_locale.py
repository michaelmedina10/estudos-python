import calendar
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR')

lista_days_and_numbers = []
for week in calendar.monthcalendar(2023, 8):
    for day, day_number in list(enumerate(week)):
        lista_days_and_numbers.append((calendar.day_name[day], day_number))

print(lista_days_and_numbers)