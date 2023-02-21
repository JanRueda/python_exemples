# Ejercicio 2.1: Conversor celsius a fahrenheit 

print('Si desea convertir celsius a fahrenheit escriba 1, encaso contrario 2')
operacion = input()

if int(operacion) < 1 or int(operacion) > 2:
    print('Opción incorrecta, fin del programa')
    exit()
else:
    if int(operacion) == 1:
        medida = 'celsius'
        print('Introduzca la cantidad de '+medida+' que desea convertir')
        celsius = int(input())
        fahrenheit = celsius * 9/5 + 32 
        print('{} ºF'.format(fahrenheit)) 
    elif int(operacion) == 2:
        medida = 'fahrenheit'
        print('Introduzca la cantidad de '+medida+' que desea convertir')
        fahrenheit = int(input())
        celsius = (fahrenheit - 32) * 5/9
        print('{} ºC'.format(celsius))