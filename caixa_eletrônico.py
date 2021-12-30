#Crie um programa que simule um funcionamente de um caixa eletrônico. No inicio
#pergunte ao usuário qual será o valor a ser sacado (número inteiro)
#e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('{:$^30}'.format('Caixa Eletrônico.'))

valor = int(input('Informe o valor do saque: R$'))
total = valor
nota50=50
nota20=20
nota10=10
nota1=1
contar50 = contar20 = contar10 = contar1 = 0

while True:
    while total>=nota50:
        total = total - nota50
        contar50 = contar50+1
    if contar50!=0:
        print(f'Saque de {contar50} notas de R$50.')
    while total>=nota20:
        total = total -nota20
        contar20 = contar20+1
    if contar20!=0:
        print(f'Saque de {contar20} notas de R$20.')
    while total>=nota10:
        total = total-nota10
        contar10 = contar10+1
    if contar10!=0:
        print(f'Saque de {contar10} notas de R$10')
    while total>=nota1:
        total = total - nota1
        contar1 = contar1+1
    if contar1!=0:
        print(f'Saque de {contar1} notas de R$1.')

    if total == 0:
        break
print('FIM')