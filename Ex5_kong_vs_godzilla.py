# Ex 5: Combate Kong vs Godzilla
# Luchamos con kong contra godzilla
import random
import os

VIDA_INICIAL_KONG = 100
VIDA_INDICIAL_GODZILLA = 100

vida_kong     = VIDA_INICIAL_KONG
vida_godzilla = VIDA_INDICIAL_GODZILLA


# Ataques Godzilla

gzll_aliento  = 20
gzll_cola     = 15
gzll_mordisco = 10

# Ataques Kong

kng_hit      = 10
kng_doblehit = 20
kng_mordisco = 15


while 1:
    os.system ("cls")
    barras_vida_kong        = int(vida_kong *10 / VIDA_INICIAL_KONG)
    barras_vida_godzilla    = int(vida_godzilla *10 / VIDA_INDICIAL_GODZILLA)

    print("kong:        [{}{}][{}/{}]".format("*" * barras_vida_kong, " " * (10 - barras_vida_kong),
                                        vida_kong,VIDA_INICIAL_KONG))
    print("godzilla:    [{}{}][{}{}]".format("*" * barras_vida_godzilla, " " * (10 - barras_vida_godzilla),
                                        vida_godzilla,"/"+str(VIDA_INDICIAL_GODZILLA)))

    var = 'Selecciona un ataque de Kong: hit(0), doblehit(1) o mordisco(2)'  
    print(var +'\n'+'-'*len(var))
    ataque_kong = int(input())

    while 1:
        if ataque_kong ==0 or ataque_kong==1 or ataque_kong==2:
            break
        else:
            var = 'Selecciona un ataque de Kong válido: hit(0), doblehit(1) o mordisco(2)'
            print(var +'\n'+'-'*len(var))
            ataque_kong = int(input())

    # print('Ataque kong: {}'.format(ataque_kong))
    # print('Continuamos programando')

    # Restamos vida a godzilla
    if ataque_kong == 0:
        print('Kong ataco con puñetazo')
        vida_godzilla -= kng_hit
    elif ataque_kong == 1:
        print('Kong ataco con doble puñetazo')
        vida_godzilla -= kng_doblehit
    elif ataque_kong == 2:
        print('Kong ataco con mordisco')
        vida_godzilla -= kng_mordisco
    # Ataca godzilla
    ataque_gzll = random.randint(0,2)

    if ataque_gzll == 0:
        print('Godzilla ataco con aliento')
        vida_kong -= gzll_aliento
    elif ataque_gzll == 1:
        print('Godzilla ataco con cola')
        vida_kong -= gzll_cola
    elif ataque_gzll == 2:
        print('Godzilla ataco con mordisco')
        vida_kong -= gzll_mordisco

    if vida_kong <= 0:
        print('Gozilla Gana')
        break
    elif vida_godzilla <= 0:
        print('Kong Gana')
        break