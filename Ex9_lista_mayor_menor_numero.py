# Ex_9: Usuario intruduce una lista de numeros separados por comas y le devuelve el mayor y el menor

print('Escribe una lista de numeros separada por comas')
lista = input()

if ',' in lista:
    separacion = lista.split(',')
    print(separacion)
    separacion2 = []
    for x in separacion:
        separacion2.append(int(x))
    print(separacion2)
    print('El número menor de la lista es {}'.format(min(separacion2)))
    print('El número mayor de la lista es {}'.format(max(separacion2)))
else:
    print('No insertaste una lista de números separados por comas')
    print('Fin del programa')

