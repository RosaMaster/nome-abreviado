from content.preposicao import listPreposicaoExclusao

class abreviacaoNomeUtil:

    def __init__(self, nome):
        self.nome = nome

    def abreviar(self):
        for i in range(len(listPreposicaoExclusao)):
            self.nome = (self.nome).replace(listPreposicaoExclusao[i], ' ')

        self.nome = self.nome.split()
        abreviado = ''
        for i in range(len(self.nome)):
            if i == 0:
                abreviado += self.nome[i] + ' '
            elif i == len(self.nome) - 1:
                abreviado += self.nome[i] + ' '
            else:
                # abreviar um item do nome e adicionar um espaço por vez e se o tamanho do nome for maior que 30 caracteres abreviar proximo item
                if len(abreviado) > 30:
                    abreviado = self.nome[i][0] + ' '
                else:
                    abreviado = self.nome[i] + ' '

        return abreviado

    def __str__(self):
        return self.abreviar()
    
    def __repr__(self):
        return self.abreviar()
    
    def __len__(self):
        return len(self.abreviar())

    