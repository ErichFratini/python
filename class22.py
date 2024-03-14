# Operadores lógicos
# and (e) or (ou) not (não) 
# or - Qualquer condição verdadeira avalia toda a expressao como verdadeira.
# Se qualque valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor
# São considerados falsy 0 0.0 '' False
# Também existe o time None que é usado para representar um não valor
entrada = input('[E]ntrar [S]air:')
senha = input('Senha: ')

senha_permitida = '123456'
# if True:
#   ...
if (entrada == 'E' or entrada == 'e') and senha == senha_permitida:
    print("Entrar")
elif entrada == 'S':
    print("Sair")

# Avaliação de curto cricuito
senha = input('Senha: ') or 'Sem senha'
print (0 or False or 0 or 'abc')