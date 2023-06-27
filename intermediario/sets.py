'''
Sets em Python são conjuntos
representados na matemática pelo diagrama de Venn.

Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno

explemplo:
set(iterável) ou {1,2,3}

'''
s1 = set()
s2 = {"Mich", 1,2,3,4}
'''
Sets são eficientes para remover valores duplicados de iteráveis:
- Eles não tem indices;
- Eles não garantem ordem;
- Eles são iteráveis(for, in, not in)
'''
l1 = [1,2,3,3,3,3,3,3,3,4]

# Ao converter para conjunto ele remove os valores duplicados
s3 = set(l1)

l2_sem_duplicidade = list(s3)
print(l1)
print(l2_sem_duplicidade)



'''
Métodos Úteis
add, update, clear, discard
'''
s4 = set()
s4.add("Michael")
s4.update(("Medina", "Michael"))
# s4.clear() limpa todo o set
s4.discard("blabla") # descarta um elemento chamado Michael no set, senão existir ele desconsidera, não quebra o código
s4.discard("Michael")
print(s4)
'''
Operadores úteis:
- união | union  - Une
- intersecção & intersection
- diferença - itens presentes somente no set da esquerda
- diferença simétrica ^, itens que não estão em ambos
'''
print("Operadores")
s5 = {1,2,3,7}
s6 = {1,2,3,4,5}

s7 = s5 | s6
s8 = s5 & s6
s9 = s5 - s6
s10 = s5 ^ s6

print(s7)
print(s8)
print(s9)
print(s10)