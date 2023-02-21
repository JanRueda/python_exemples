# Ex3: Piedra, Papel, Tijera
# tijeras cortan papel
# papel envuelve piedra
# piedra rompe tijeras



import random

election_bot = random.randint(0,2)

print('Elija su opción: piedra(0), papel(1), tijera(2)')

election_human = int(input())

if election_human < 0 or election_human > 2:
    print('No seleccionó la opción correcta, fin del juego')
    exit()
else:
    # print('Seleccionó la opción correcta')
    # print('humano: {}'.format(election_human))
    # print('bot: {}'.format(election_bot))
   
    resultado_human = ''
    resultado_bot = ''

    if election_human == 0:
        resultado_human = 'piedra'
    elif election_human == 1:
        resultado_human = 'papel'
    elif election_human == 2:
        resultado_human = 'tijeras'

    if election_bot == 0:
        resultado_bot = 'piedra'
    elif election_bot == 1:
        resultado_bot = 'papel'
    elif election_bot == 2:
        resultado_bot = 'tijeras'

    print('tu: ' + resultado_human + ', el bot: ' + resultado_bot)

    if resultado_human == resultado_bot:
        print('Empate')
    elif resultado_human == 'tijeras' and resultado_bot == 'papel':
        print('Ganaste')
    elif resultado_human == 'papel' and resultado_bot == 'piedra':
        print('Ganaste')
    elif resultado_human == 'piedra' and resultado_bot == 'tijeras':
        print('Ganaste')
    else:
        print('Perdiste')