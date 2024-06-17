from content.data import data
from model.update_name import UpdateName

# Objeto JSON
print('\n******* objeto JSON ******')
print(data)
print(len(data))
print(type(data))
print('**************************\n')

if len(data['nome']) > 50:
    updateNomeTm = UpdateName(data['nome']).__repr__()

    # Verifica se o nome está igual na base TM
    # Se não estiver, atualiza o nome

    # if len(updateNomeTm) > 30:
        # updateNomeQ4 = UpdateName(data['nome'], 30).__repr__()

        # Verifica se o nome está igual na base Q4
        # Se não estiver, atualiza o nome


