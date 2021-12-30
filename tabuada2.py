#Faça um programa que mostre a tabuada de vários números, um de cada vez para
#cada valor digitado pelo usuário. O programa será interrompido quando o
#número solicitado for negativo.
print('{:=^21}'.format('\033[36mTABUADA\033[m'))

cont = tabuada = num = 0

while True:
    print('='*20)
    num = int(input('Informe um número para tabuada:'))
    if num<0:
        print('\033[32mFim do programa.\033[m')
        break
    for cont in range(0, 11):
        tabuada = cont * num
        print(cont, 'x', num, '=', tabuada)
