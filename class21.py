# Operadores lógicos
# and (e) or (ou) not (não) 
# and - Todas as condições precisam ser verdadeiras
# Se qualque valor for considerado falso, a expressão inteira será avaliada naquele valor
# São considerados falsy 0 0.0 '' False
# Também existe o time None que é usado para representar um não valor
entrada = input('[E]ntrar [S]air:')
senha = input('Senha: ')

senha_permitida = '123456'
# if True:
#   ...
if entrada == 'E' and senha == senha_permitida:
    print("Entrar")
elif entrada == 'S':
    print("Sair")

# Avaliação de curto cricuito
print (True and False and True)