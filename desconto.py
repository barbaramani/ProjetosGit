#exercicio12
#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
print('{:*^20}'.format('Desconto de 5%'))
valor=float(input('Informe o valor real do produto: R$ '))
desconto=float(valor-(valor*0.05))

print('O valor do produto era de R${}. E com desconto de 5% ficou R${:.2f}'.format(valor, desconto))

print('='*50)
#Informar outro desconto
desconto2=float(input('Informe o novo desconto desconto:'))
percentual=float(desconto2/100)

print('Com desconto de {:.0f}%, novo valor com desconto é de R${:.2f}'. format(desconto2,valor-(valor*percentual)))
