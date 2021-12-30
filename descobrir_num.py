#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
#e peça para o usuário descobrir qual foi o número.
#O programa deverá escrever na tela se o usuário ganhou ou perdeu
print('{:#^30}'.format('Adivinha um número'))
print('-=-'*15)

import random
import time
numero = random.randint(0,5)

adivinhe = int(input('Escolha um número:'))
print('PROCESSANDO...')
time.sleep(3)

if numero == adivinhe:
    print('Parabéns, você acertou!')
else:
    print('Você errou. O número era {}'.format(numero))
print('FIM DE JOGO')
