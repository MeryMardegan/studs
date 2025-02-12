"""
Sistema de perguntas e respostas
"""

perguntas = [
    {
        'pergunta': 'Quanto é 2 + 2?',
        'Opções': ['3', '4', '5', '6'],
        'resposta': 1
    },
    {
        'pergunta': 'Quanto é 3 * 2?',
        'Opções': ['3', '4', '5', '6'],
        'resposta': 3
    },
    {
        'pergunta': 'Quanto é 4 - 2?',
        'Opções': ['2', '3', '5', '6'],
        'resposta': 0
    },
    ]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['pergunta'])

    opcao = pergunta['Opções']
    for i, opcao in enumerate(opcao):
        print(f'alternativa {i})', opcao)

    resposta = input('\nSua resposta: \n')

    if resposta.isdigit():
        resposta_int = int(resposta)
        if 0 <= resposta_int < len(pergunta['Opções']):
            if resposta_int == pergunta['resposta']:
                qtd_acertos += 1
                print('Acertou a resposta 😊\n')
            else:
                print('Errou a resposta 😢\n')
        else:
            print('Alternativa inválida\n')
    else:
        print('Entrada inválida! Digite um número.\n')

print(f'Você acertou {qtd_acertos} de {len(perguntas)} perguntas')