#Crie um programa que mostre o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todas as letras minúsculas
# - Quantas letras aotodo sem considerar os espaços
# - Quantas letras tem o primeiro o primeiro nome

print('{:*^21}'.format('Manipulando Texto'))
nome = str(input('Informe seu nome:')).strip() #neste caso pode inserir espaço antes ou depois do nome para não contar.
print('Quantidade de caracteres é {}'.format(len(nome)))
print('Letras maiúsculas:',nome.upper())
print('Letras minúsculas:', nome.lower())
print('Todas de letras sem condiderar o espaço é de {}'.format(len(nome)- nome.count(' ')))

primeironome = nome.split()
print('O primeiro nome {} tem {} letras'.format(nome.split()[0],len(primeironome[0])))

#outro jeito de encontrar o número de letras do primeiro nome
print('O primeiro nome tem {} letras'.format(nome.find(' ')))

#neste caso, pede para encontrar o primeiro espaço