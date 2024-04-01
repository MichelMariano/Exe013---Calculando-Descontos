#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5%
#de desconto.

preço = float(input('Qual é o Preço do Produto? R$ '))
novo = preço - (preço * 5 / 100)

print('O produto teve um desconto de 5% e se novo valor é R$ {:.2f} '.format(novo))
