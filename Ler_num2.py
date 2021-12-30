#exercicio06
# Criar um programa que leia um número e mostre seu dobro, triplo e a raiz
n=int(input('Escolha um número:'))
dobro=n*2
triplo=n*3
raiz=n**(1/2)
print('O número escolhido foi  {}\n Seu dobro é {} \n O triplo é {} \n a raiz é {}'
      .format(n, dobro, triplo, raiz))
print('Outra forma de calcular a raiz', pow(n,(1/2)))
