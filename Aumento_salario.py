#exercicio13
#Faça um algoritmo que leia salário de um funcionário e mostre seu novo salário, com
#15% de aumento.
print('{:#^18}'.format('Novo salário'))
salario=float(input('Informe seu salário: R$'))
aumento=float(input('Informe o percentual de aumento:'))
novosal=float(salario+(salario*(aumento/100)))

print('O salário era R$ {:.2f}, e com aumento de {:.0f}%, ficou R${:.2f}'.format(salario, aumento, novosal))

print('#'*20)