
def concatenar(string_inicial):
    ## A variavel valor final esta sendo usada em outro scopo pela interna, por ser um scopo maior da concatenar eu posso LER
    ## Mas não posso alterar
    valor_final = string_inicial
    def interna(valor_a_concatenar):
        # usando nonlocal resolvemos isso
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar("a")
print(c("b"))
print(c("c"))
print(c("d"))