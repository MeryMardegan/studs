import random


print('Bem vindo ao gerador de CPF')

gerando_cpf = ''
for i in range(9):
    gerando_cpf += str(random.randint(0, 9))

contador_regressivo_1 = 10
resultado_1 = 0
for digito in gerando_cpf:
    resultado_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = gerando_cpf + str(digito_1)
contador_regressivo_2 = 11

resultado_2 = 0
for digito in dez_digitos:
    resultado_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_algoritmo = gerando_cpf + str(digito_1) + str(digito_2)
print(f'CPF gerado pelo algoritmo: {cpf_gerado_pelo_algoritmo}')
