def adivinar(intentos):

    import random

    numAleatorio = random.randint(0, 100)


    for i in range(0, intentos):
        numero = input('Adivine el numero que cree que es ')
        numero = int(numero)

        if numAleatorio == numero:
            print("El numero es correcto")
            break
        elif numAleatorio > numero:
            print('Tu estimación es muy baja.')
        elif numAleatorio < numero:
            print('Tu estimación es muy alta.')

        intentos = intentos + 1

while True:
    intentos = int(input('Cantidad de intentos: '))
    if intentos <= 0:
        print('La cantidad de intentos debe ser mayor a 0.')
    else:
        break

adivinar(intentos)