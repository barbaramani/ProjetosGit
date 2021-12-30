#Crie um programa que mostre na tela todos os pares que estão entre 1 e 50
print('{:#^20}'.format('\033[7;30mPARES\033[m'))
for c in range(2,51,2):
    print(c, end=' ')
print('FIM')