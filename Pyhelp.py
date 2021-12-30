#Faça um mini sistema que utiliza o Interactive Help do Python. O usuário vai digitar o comando
# e o manual vai parecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# OBS: use cores.


from time import sleep
print('\033[42m~'*27)
print('\033[42m  SISTEMA DE AJUDA PyHELP  ')
print('\033[42m~'*27)
print('\033[m')

while True:

    funcao = input('Função ou Biblioteca:')
    if funcao.upper()!='FIM':

        print('\033[44m~'*(len(f'Acessando o manual do comando {funcao}')+6))
        print(f"\033[44m  Acessando o manual do comando '{funcao}'")
        print('\033[44m~'*(len(f'Acessando o manual do comando {funcao}')+6))
        print('\033[m')
        sleep(0.5)

        print('\033[7:40m')
        help(funcao)
        print('\033[m')

    else:
        print('\033[41m~'*(len('Até logo')+2))
        print('\033[41m Até logo!')
        print('\033[41m~' * (len('Até logo')+2))
        break