import re

chave = "c1327624"
tipo, numeros = re.match(r"^(c|f)([0-9]{7})$", chave).groups()
print(tipo, numeros)
