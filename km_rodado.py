#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print('{:*^30}'.format('ALUGUEL DE CARRO'))

km=float(input('Quantos quilômetros rodados?'))
dias=int(input('Quantos dias alugado?'))

valorkm=km*0.15
valordias=dias*60
preco=valorkm+valordias

print('Você rodou {:.0f}Km por {} dias. O preço final para pagamento é de: R$ {:.2f}'
      .format(km, dias, preco))

print('*'*30)