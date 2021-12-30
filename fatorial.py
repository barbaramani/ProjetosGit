#Faça um programa que leia um número qualquer e faça seu fatorial.(fazer com while e com for)
n = int(input('Informe um número:'))
contador = n #contador começa com n. O fatorial como com n.

contar = 1
for c in range(1,n+1):
    contar = contar*c
print('O fatorial de {} é {}.'.format(n, contar))