#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5%
#de desconto.

preço = float(input('Qual é o Preço do Produto? R$ '))
novo = preço - (preço * 5 / 100)

print('O produto teve um desconto de 5% e se novo valor é R$ {:.2f} '.format(novo))



-----------------------------------

# desconto a vista e acrescimo a prazo

prod = input('Digite o Produto: ')
preço = float(input('Qual é o Preço do Produto? R$ '))
novo = preço - (preço * 5 / 100)
prazo = preço + (preço * 10/100)
print('=' * 90)
print('O produto {} tem de 5% de desconto para pagamento a vista e se novo valor é R$ {:.2f} '.format(prod, novo))
print('-' * 90)
print('O produto {} pagando a prazo, terá um acrescimento de 10% e passara a valer R$ {} '.format(prod, prazo))
print('=' * 90)
