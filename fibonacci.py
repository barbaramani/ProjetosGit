#Escreva um programa que leia um número n inteiro qualquer, e mostre na tela
# os n primeiros elementos de uma Sequência de Fibonacci.
'''
0 - 1 - 1 - 2 - 3 - 5
t1 - t2 - t3
    t1 - t2 - t3'''
print('{:*^30}'.format('Sequência de Fibonacci'))

n = int(input('Informe quantos termos:'))
t1 = 0
t2 = 1
contador = 3 #começa com 3 pois já possuímos o t1 = 01 e o t2 = 1.(Sempre começa com 0 e 1).

print('{} -> {} ->'.format(t1,t2), end=' ')

while contador<=n:
    t3 = t1+t2
    print('{} ->'.format(t3),end=' ')
    t1 = t2
    t2 = t3
    contador = contador+1
print('FIM')