from data.data import data
from model.validador_nome_cliente import ValidadorNomeCliente

# Objeto JSON
print('\n******* objeto JSON ******')
print(data)
print(len(data))
print(type(data))
print('**************************\n')



validador_nome_cliente = ValidadorNomeCliente()

nome_abreviado = validador_nome_cliente.validacao_comprimento_nome(data['nome'], 30)


print(nome_abreviado)