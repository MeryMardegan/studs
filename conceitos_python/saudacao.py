horario = input("Que horas são? ")

try:
    horario = int(horario)
    if horario >= 0 and horario <= 11:
        print("Bom dia")

    elif horario >= 12 and horario <= 17:
        print("Boa tarde")
    
    else:
        print("Boa noite")

except:
    print("Por favor, apenas número inteiros")