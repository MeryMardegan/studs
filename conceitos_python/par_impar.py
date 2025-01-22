print ("Digite um número inteiro")
numero = input()
if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")