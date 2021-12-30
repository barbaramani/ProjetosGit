#exercicio11
#Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área
#e a quantidade de tinta necessária para pintá-la.
#Sabendo que cada lata de tinta pinta uma área de 2m quadrados
print('{:=^21}'.format("Cálculo da área"))
b=float(input('Informe o tamanho da base = '))
h=float(input('Infome o tamnho da altura = '))
s=b*h
tinta=s/2

print('Para um dimensão de {}x{} com uma área de {}m², iremos precisar de {} litros de tinta.'
      .format(b,h,s,tinta))

print('='*21)
