"""
Crie funções que duplicam, triplicam e quadruplicam um número
o número recebido como parâmetro
"""

def multiplicador(numero, multiplicador):
    return numero * multiplicador
print (multiplicador(2, 2))
print (multiplicador(2, 3))
print (multiplicador(2, 4))

def criar_funcao_multiplicadora(multiplicador):
    def multiplicador_numero(numero):
        return numero * multiplicador
    return multiplicador_numero

duplica = criar_funcao_multiplicadora(2)
triplicar = criar_funcao_multiplicadora(3)
quadriplicar = criar_funcao_multiplicadora(4)

print (duplica(2))
print (triplicar(2))
print (quadriplicar(2))