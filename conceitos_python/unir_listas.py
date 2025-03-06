# Exercício: unir listas
# Crie uma função zipper que unirá duas listas na ordem
# Usar todos os valores da menor lista
# Exemplo:
def zipper(lista1, lista2):
    intervalo_maximo = min(len(lista1), len(lista2))
    return [
        (l1[i], l2[i]) for i in range(intervalo_maximo)
    ]

l1 = ["Salvador", "Recife", "Fortaleza", "Natal"]
l2 = ["Bahia", "Pernambuco", "Ceará"]

print (zipper(l1, l2)) 
print (list(zip(l1, l2))) # Usando a função zip do Python

from itertools import zip_longest
print (list(zip_longest(l1, l2))) # Usando a função zip_longest do Python