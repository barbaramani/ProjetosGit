#Crie um programa que leia um frase qualquer e diga se ela é um palíndromo, desconsidetando os espaços.
#Desconsiderar acento e espaços.
#Apos a sopa / a sacada da casa /a torre da derrota / o lobo amo o bolo / anotaram a data da maratona
print('{:#^30}'.format('\033[1mPalíndromo\033[m'))

palavra = input('Escreva uma palavra ou frase:')
letra = palavra.replace(' ','') #poderia colocar dentro do FOR
print(letra)
'''
for caracter in palavra:
    print(caracter, end =' ')
'''

if letra[::-1] == letra:
    print('\n\033[33m{} é um \033[4mPalíndormo!\033[m'.format(palavra))
else:
    print('\n\033[35m{} não é Palíndromo.\033[m'.format(palavra))

print('FIM')