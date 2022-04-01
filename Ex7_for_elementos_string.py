# Ex 7: For - Indicar los elementos que componen un string
# Mayúsculas, minúsculas, letras, espacios y puntos

var = 'Esta Casa tiene pictogramas..'

### Total letras
total_letras = len(var.split())
print('La frase tiene un total de {} letras'.format(total_letras))

### Espacios
espacios = 0
puntos   = 0
mayus    = 0
minus    = 0

for i in var:
    if i == ' ':
        espacios += 1
    if i == '.':
        puntos += 1
    if i.isupper():
        mayus += 1
    if i.islower():
        minus +=1


print('Espacios totales en el string: {}'.format(espacios))
print('Puntos totales en el string: {}'.format(puntos))
print('Letras mayúsculas totales en el string: {}'.format(mayus))
print('Letras minúsculas totales en el string: {}'.format(minus))