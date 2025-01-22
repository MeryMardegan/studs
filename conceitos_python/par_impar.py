print ("Digite um número inteiro")
numero = input()
if numero.isdigit():
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")
else:
    print ("Digite um número inteiro válido")