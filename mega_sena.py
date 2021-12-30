#Faça um programa que ajude um jogador da mega sena a cria palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60,
#para cada jogo cadastrando tudo em uma lista composta.
print('{:=^21}'.format('Mega Sena'))

num = []
mega = []
import random
import time

jogo = int(input('Quantos jogos?'))
total = 1

while total<=jogo:
    for i in range(6):
        num.append(random.randint(1,60))
    num.sort()
    mega.append(num[:])
    num.clear()
    total=total+1

for i, l in enumerate(mega):
    time.sleep(1)
    print(f'Jogo número {i+1}:{l}')