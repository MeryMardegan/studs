nome = input("Digite seu primeiro nome: ")
if len(nome)>=1 and len(nome) <= 4:
    print("Seu nome é curto")
elif len(nome) >= 5 and len(nome) <= 6:
    print("Seu nome é normal")
elif len(nome) >= 7 and len(nome) <= 15:
    print("Seu nome é muito grande")
else:
    print("Digite um nome válido")