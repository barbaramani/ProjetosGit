#Escreva um programa para aprovar um empréstimo para compra de uma casa.
#O programa vai peguntar o valor da casa, o salário e quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que não pode exceder de 30% do salário,
#ou então o empréstimo será negado.

print('{:#^30}'.format('\033[31mEmpréstimo\033[m'))
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
ano = int(input('Quantos anos de prestação?'))

prestacao = ano*12
prest = casa/prestacao
excedente = salario*0.30

import time
print('Calculando...')
time.sleep(2)

if excedente>prest:
    print('\033[34mEmpréstimo Aprovado! \033[mSua prestação é de R${:.2f} em {} anos.'.format(prest,ano))
else:
    print('\033[31mEmpréstimo não aprovado.\033[m')
print('FIM')