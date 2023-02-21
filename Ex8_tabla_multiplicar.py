# Ex_8: Usuario elige un número y se le devuelve la tabla de multiplicar de dicho numero
print('Elige un número y te doy su tabla de multiplicar')
numero = int(input())
for i in range(1,11):
    resultado = i*numero
    print(str(i)+'x'+str(numero)+'='+str(resultado))