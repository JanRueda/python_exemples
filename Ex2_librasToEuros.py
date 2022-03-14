# Ejercicio 2.1: Conversor libras a euros 
# Tipo de cambio fijo 1,19 euros por libra estarlina

tipo_cambio = 1.19

print('Si desea convertir libras a euros escriba 1, encaso contrario 2')
operacion = input()

if int(operacion) < 1 or int(operacion) > 2:
    print('Opción incorrecta, fin del programa')
    exit()
else:
    if int(operacion) == 1:
        moneda = 'euros'
        print('Introduzca los '+moneda+' que desea convertir')
        euros = int(input())
        libras = euros/tipo_cambio
        print(libras)
    elif int(operacion) == 2:
        moneda = 'libras'
        print('Introduzca las '+moneda+' que desea convertir')
        libras = int(input())
        euros = tipo_cambio*libras
        print(euros)




