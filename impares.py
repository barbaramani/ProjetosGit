#Faça um programa que calcule a soma de todos os números impares que são múltiplos de três
#e que se encontram no intervalo de 1 a 500.
print('{:#^20}'.format('\033[35mNúmeros ímpares\033[m'))

soma = 0
contador = 0
for c in range(1,501,2):
    if c%3==0:
        soma = soma+c
        contador = contador+1
print(soma)
print('São',contador, 'valores ímpares e divisíveis por 3.')