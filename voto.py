#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano do nascimento
# de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO
# nas eleições.
print('{:=^23}'.format('\033[7:30;40mVOTO\033[m'))


def voto(ano):
    from datetime import date
    atual = date.today().year
    if 1957<=ano<=2003:
        print(f'Com {atual-ano} anos:\033[34m VOTO OBRIGATÓRIO\033[m')
    elif ano==2005 or ano<=1956:
        print(f'Com {atual-ano} anos: \033[32mVOTO OPCIONAL\033[m')
    else:
        print(f'Com {atual-ano} anos: \033[33mVOTO NEGADO\033[m')

print()
ano = int(input('Em que ano você nasceu?'))
voto(ano)