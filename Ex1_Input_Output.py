# Ejercicio 1: Indicar cual es el número más grande y el más pequeño de los tres números introducidos por el usuario

print('Inserte el primer número')
numero_1 = int(input())
print('Inserte el segundo número')
numero_2 = int(input())
print('Inserte el tercer número')
numero_3 = int(input())

print('El primer número es {}'.format(numero_1))
print('El segundo número es {}'.format(numero_2))
print('El tercer número es {}'.format(numero_3))

numero_mayor = max(numero_1,numero_2,numero_3)
numero_menor = min(numero_1,numero_2,numero_3)

print('El número más grande es: {}'.format(numero_mayor))
print('El número más pequeño es: {}'.format(numero_menor))