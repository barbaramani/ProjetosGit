#Faça um programa que leia um número inteiro e diga se ele é primo ou não.

'''
if num!=2 and num%2==0:
    print('{} não é primo'.format(num))
elif num!=3 and num%3==0:
    print('{} não é primo'.format(num))
elif num!=5 and num%5==0:
    print('{} não é primo'.format(num))
elif num!=7 and num%7==0:
    print('{} não é primo'.format(num))
else:
    print('{} - Este número é primo.'.format(num))

print('FIM')
'''

print('{:=^30}'.format('Número Primo'))

num = int(input('Entre com um número:'))
tot = 0
for c in range(1,num+1):
    if num%c==0:
        print('\033[34m',end=' ')
        tot = tot+1
    else:
        print('\033[m', end=' ')
    print(c, end='')
print('\n\033[mQuantidade de números divisíveis é {}'.format(tot))
if tot==2:
    print('É primo')
else:
    print('Não é primo.')