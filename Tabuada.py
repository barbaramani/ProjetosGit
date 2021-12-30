# exercicio09
# Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada
n = int(input('número:'))

mult = 0

for mult in range(0, 11):
    result = n * mult
    mult += 1
    print(result)
#Outro jeito
print('{:=^20}'.format('Tabuada'))
print('='*20)

#{:2} PARA TER DOIS DÍGITOS E FICAR ALINHADO
print('{} x {:2} = {}'.format(n,1,n*1))
print('{} x {:2} = {}'.format(n,2,n*2))
print('{} x {:2} = {}'.format(n,3,n*3))
print('{} x {:2} = {}'.format(n,4,n*4))
print('{} x {:2} = {}'.format(n,5,n*5))
print('{} x {:2} = {}'.format(n,6,n*6))
print('{} x {:2} = {}'.format(n,7,n*7))
print('{} x {:2} = {}'.format(n,8,n*8))
print('{} x {:2} = {}'.format(n,9,n*9))
print('{} x {:2} = {}'.format(n,10,n*10))
print('{:=^20}'.format(''))
