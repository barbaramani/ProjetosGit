#exercicio08
#Escreva um programa que leia o valor em metros, e converta ele em centímetros e milímetros
m=float(input('Valor em metros = '))
dm=m*10
cm=m*100
mm=m*1000
km=m/1000
hm=m/100
dm=m/10

print('Metros = {}\n Decímento = {} \n Centímetros = {:.0f}\n Milímetros= {:.0f} \n '
      'Km = {} \n hm = {} \n dm= {}'.format(m,dm,cm,mm,km,hm,dm))
