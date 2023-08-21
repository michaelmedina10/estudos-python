from string import Template


# o delimiter padrão é $ logo o texto estaria $nome, $email, por exemplo, é possivel mudar caso seja necessário
texto_email_exemplo = '''

    Prezado ${nome}

    Sua conta bancária foi excluida com sucesso

'''

template = Template(texto_email_exemplo)
texto_email = template.substitute(nome='Michael')
print(texto_email)