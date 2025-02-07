import os
lista = []

while True:
    print('Selecione uma opção:')
    opcao = input('[I]nserir item\n[R]emover item\n[L]istar itens\n[S]air\n')

    if opcao.upper() == 'I':
        item = input('Digite o item a ser inserido: ')
        lista.append(item)
        os.system('cls' if os.name == 'nt' else 'clear')
        for indice, valor in enumerate(lista):
                print('lista atual:' f'{indice}: {valor}')
    elif opcao.upper() == 'R':
        if len(lista) == 0:
            print('Lista vazia')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            for indice, valor in enumerate(lista):
                print(f'lista atual: {indice}: {valor}')
            item = input('Digite o item a ser removido: ')
            if item.isdigit():
                indice = int(item)
                if 0 <= indice < len(lista):
                    del lista[indice]
                    for indice, valor in enumerate(lista):
                        print(f'lista atual: {indice}: {valor}')
                else:
                    print('Índice inválido')
            elif item in lista:
                del lista[item]
                os.system('cls' if os.name == 'nt' else 'clear')
                for indice, valor in enumerate(lista):
                    print(f'lista atual: {indice}: {valor}')
            else:
                print('Item não encontrado')
    elif opcao.upper() == 'L':
        if len(lista) == 0:
            print('Lista vazia')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            for indice, valor in enumerate(lista):
                print(f'lista atual: {indice}: {valor}')
    elif opcao.upper() == 'S':
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Opção inválida')