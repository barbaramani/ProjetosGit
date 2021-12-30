#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre
#os 10 primeiros termos dessa progressão.
print('{:=^50}'.format('\033[36mTERMOS DA PA\033[m'))

a1 = int(input('Informe o primeiro termo:'))
r = int(input('Informe a razão:'))
an = a1+(10-1)*r #para calcular o enésimo termo da PA - an=(n-1)*r
print(an)

print('\033[1;30mOs 10 primeiros termos da PA são:\033[m')
for c in range(a1,an+r,r):
    print( c, end=' -> ')
print('\033[1;30mACABOU\033[m')