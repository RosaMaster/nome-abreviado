import json
from utils.util import abreviacaoNomeUtil

class UpdateName:
    def __init__(self, name):
        self.name = name

    # Abreviando o nome
    def abreviacaoNome(self):
        
        name_abrev = abreviacaoNomeUtil(self.name).__repr__().strip()

        print('******* abreviando o nome ******')
        print(name_abrev)
        print(type(name_abrev))
        print(name_abrev.__len__())
        print("********************************\n")

        return name_abrev
    
    def __str__(self):
        return self.abreviacaoNome()
    
    def __repr__(self):
        return self.abreviacaoNome()

