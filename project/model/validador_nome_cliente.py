from model.abrevia_nome import AbreviaNome

class ValidadorNomeCliente:

    def validacao_comprimento_nome(self, nome_completo, limite):
        ''' Função que valida o comprimento de um nome completo '''
        
        if len(nome_completo) > limite:
            
            abrevia_nome = AbreviaNome()

            nome_completo = abrevia_nome.regex_replace(nome_completo)

            if len(nome_completo) > limite:

                nome_completo = abrevia_nome.abrevia_nome(nome_completo, limite)
        
        return nome_completo
    
