#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
#em um dicionário e todos os dionários em uma lista. no final, mostre:
#a)Quantas pessoas foram cadastradas / b)A média de idade do grupo/
# c)Uma lista com todas as mulheres/ d) Uma lista com todas as pessoas com idade acima da média.
print('{:=^20}'.format('Cadastro'))
cadastro = dict()
total = 0
lista_cad = []
lista_mulheres = []
lista_acimamedia = []
media = 0
soma_idade = 0

while True:
    cadastro.clear() #para apagar antes de uma pessoa nova
    cadastro['nome'] = str(input('Nome:'))
    cadastro['sexo'] = str(input('Sexo [F/M]:')).upper().strip()[0]
    while cadastro['sexo'] not in 'FM':
        print('Erro! Digite F ou M')
        cadastro['sexo'] = str(input('Sexo [F/M]:')).upper().strip()[0]
    cadastro['idade'] = int(input('Idade:'))

    continua = str(input('Deseja continuar [S/N]:')).upper().strip()
    while continua not in 'SN':
        print('Erro! Digite S OU N.')
        continua = str(input('Deseja continuar [S/N]:')).upper().strip()

    lista_cad.append(cadastro.copy())
    total = total+1
    soma_idade = (soma_idade+ cadastro['idade'])
    media = soma_idade/total
    if cadastro['sexo'] in 'Ff':
        lista_mulheres.append(cadastro['nome'])
    if cadastro['idade']>=media:
        lista_acimamedia.append(cadastro['nome'])

    if continua in 'N':
        break

print('-='*30)
print(lista_cad)
print(f'a) O número de pessoas cadastradas foi: {total}')
print(len(cadastro))
print(f'b) A média da idade do grupo é: {media} anos.')
print(f'c) A lista de mulheres cadastradas é {lista_mulheres}')
print(f'd) A lista de pessoas com idade acima da média é: {lista_acimamedia}')

for p in lista_cad:
    if p['idade']>=media:
        for k,v in p.items():
            print(f'{k} = {v}', end= ' ')
        print()

