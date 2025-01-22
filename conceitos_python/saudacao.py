horario = input("Que horas são? ")
if horario.isdigit():
    horario = int(horario)
    if horario < 0 or horario > 23:
        print("Horário inválido")
    elif horario < 12:
        print("Bom dia")
    elif horario > 12 and horario < 18:
        print("Boa tarde")
    else:
        print("Boa noite")