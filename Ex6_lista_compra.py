# Ex 6: Lista de la compra

lista = []

while 1:

    if len(lista) == 0:
        print('Sin elementos en la lista de la compra')
    else:
        print(lista)

    print('¿Quieres añadir un elemento a la lista de la compra?\npulsa (q) para salir')
    elemento = input()
    print(elemento)
    if elemento == 'q':
        print('Fin del programa')
        break
    else:
        if elemento in lista:
            print('El elemento ya se añadió a la lista')
        else:
            print('Elemento añadido a la lista')
            lista.append(elemento)


