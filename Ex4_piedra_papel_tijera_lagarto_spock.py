# Ex4: Piedra, Papel, Tijera, lagarto, spock

# tijeras cortan papel
# papel tapa piedra
# piedra aplasta a lagarto
# lagarto envenena a spock
# spock rompe tijeras
# tijeras decapitan a lagarto
# lagarto devora papel
# papel desautoriza a spock
# spock vaporiza piedra
# piedra aplasta a tijeras

import random

election_bot = random.randint(0,3)

print('Elija su opción: piedra(0), papel(1), tijera(2), lagarto(3) o spock(4)')

election_human = int(input())

if election_human < 0 or election_human > 4:
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
    elif election_human == 3:
        resultado_human = 'lagarto'
    elif election_human == 4:
        resultado_human = 'spock'

    if election_bot == 0:
        resultado_bot = 'piedra'
    elif election_bot == 1:
        resultado_bot = 'papel'
    elif election_bot == 2:
        resultado_bot = 'tijeras'
    elif election_bot == 3:
        resultado_bot = 'lagarto'
    elif election_bot == 4:
        resultado_bot = 'spock'

    print('tu: ' + resultado_human + ', el bot: ' + resultado_bot)

    if resultado_human == resultado_bot:
        print('Empate')
    elif resultado_human == 'tijeras' and resultado_bot == 'papel' or resultado_human == 'tijeras' and resultado_bot == 'lagarto':
        print('Ganaste')
    elif resultado_human == 'papel' and resultado_bot == 'piedra' or resultado_human == 'papel' and resultado_bot == 'spock':
        print('Ganaste')
    elif resultado_human == 'piedra' and resultado_bot == 'tijeras' or resultado_human == 'piedra' and resultado_bot == 'lagarto':
        print('Ganaste')
    elif resultado_human == 'lagarto' and resultado_bot == 'spock' or resultado_human == 'lagarto' and resultado_bot == 'papel':
        print('Ganaste')
    elif resultado_human == 'spock' and resultado_bot == 'tijeras' or resultado_human == 'spock' and resultado_bot == 'piedra':
        print('Ganaste')
    else:
        print('Perdiste')