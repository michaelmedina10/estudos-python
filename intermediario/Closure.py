from typing import Callable

'''
Closure e Funções que retornam outra funções
'''

def criar_saudacao(saudacao: str) -> Callable[[],str]:
    def saudar(nome: str) -> str:
        return f'{saudacao}, {nome}!!!'
    return saudar

falar_bom_dia = criar_saudacao("Bom dia")
falar_boa_noite = criar_saudacao("Bom noite")

'''
Closure ocorre quando realizamo a chamada da função e ele faz o "fechamento" da função principal:
a funcao principal é a criar_saudacao;
dentro criamos outra chamada saudar;
quando chamo a funcao criar saudacao, passando uma saudacao, e retorno a funcao saudar, sem executar, sem os parenteses
o python salva na memória, os valores da funcao principal, o estado até que ela seja executada por completo;
quando guardei em uma variável fala_bom_dia e depois invoquei passando o nome Michael, ele literalmente retorna para a linha
9 com return e ai sim retorna uma string, com o Bom dia, que foi o argumento passado anteriormente
'''
print(falar_bom_dia("Michael"))
print(falar_boa_noite("Micael L. Jackson"))