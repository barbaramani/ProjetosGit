#Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerra quando ele disser que quer mostrar 0 termos.

a1 = int(input('Informe o primeiro termo:'))
r = int(input('Informe a razão:'))
n = int(input('Quantos termos?'))
contador = 1
termo = a1
mais_termos = n
total = 0

while mais_termos!=0:
    total = total+mais_termos
    while contador<=total:
        contador = contador+1
        termo = termo+r
        print(termo)
    mais_termos = int(input('Quantos termos a mais?'))
print(total)
