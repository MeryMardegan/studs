# Peça para o usuário digitar seu nome
nome = input('Digite seu nome: ')
# Peça para o usuário digitar sua idade
idade = input('Digite sua idade: ')

# Se o nome e a idade forem digitados:
if nome and idade:
    #Exiba:
    print (f'Seu nome é {nome}')
    print (f'Sua idade é {idade}')
    print (f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print ('Seu nome contém espaço')
    else:
        print ('Seu nome não contém espaço')
    print (f'Seu nome tem {len(nome)} letras')
    print (f'A primeira letra do seu nome é {nome[0]}')
    print (f'A última letra do seu nome é {nome[-1]}')
# Se nada for digitado em nome ou idade:
else:
    print ('Nada foi digitado, tente novamente')
