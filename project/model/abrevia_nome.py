import re

class AbreviaNome:

    def regex_tratando_nome(self, nome_completo):
        ''' Função que trata um nome completo ''' 

        characteres = str.maketrans("@áàâãäéèêëíìîïóòôõöúùûüçÁÀÂÃÄÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÛÜÇ", "aaaaaaeeeeiiiiooooouuuucAAAAAEEEEIIIIOOOOOUUUUC")

        nome_string = nome_string.translate(characteres)

        

        return nome_string

    def regex_replace(self, nome_completo):
        ''' Função que remove preposições e caracteres especiais de um nome completo '''

        regex_expressao_replace = re.compile(r"\b[d][aeiou]s?\b|\b[aeou]\b|[@&*#%$!,.;:()_+=-]", re.IGNORECASE)

        nome_sem_preposicao = regex_expressao_replace.sub(' ', nome_completo)

        nome_sem_preposicao = nome_sem_preposicao.split()

        return ' '.join(nome_sem_preposicao)
    
    
    def regex_erase_sobrenome_abreviado(self, nome_completo):
        ''' Função que remove sobrenomes abreviados de um nome completo '''

        regex_expressao_erase = re.compile(r"\b \w ", re.IGNORECASE)

        nome_sem_sobrenome_abreviado = regex_expressao_erase.sub(' ', nome_completo, 1)

        return nome_sem_sobrenome_abreviado


    def abreviacao_nome_recursiva(self, lista, limite, i):
        ''' Função que abrevia um nome recursivamente '''

        if sum(len(item) for item in lista) + (len(lista) - 1) > limite and i > 1:

            lista[i] = lista[i][0]

            self.abreviacao_nome_recursiva(lista, limite, i - 1)
        
        return ' '.join(lista)
    

    def abrevia_nome(self, nome_completo, limite):
        ''' Função que abrevia um nome '''

        lista_nome_abreviado = nome_completo.split()

        string_nome_abreviado = self.abreviacao_nome_recursiva(lista_nome_abreviado, limite, i = len(lista_nome_abreviado) - 2)

        for i in range(len(lista_nome_abreviado) - 3):

            if len(string_nome_abreviado) > limite:

                string_nome_abreviado = self.regex_erase_sobrenome_abreviado(string_nome_abreviado)

        return string_nome_abreviado[:limite]

        