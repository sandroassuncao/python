preço = float(input('preço do produto:'))
desconto = preço * 5/100 
preço2 = preço - desconto
print('preço do produto é: R$ {} e o valor do desconto é: R$ {} e o novo preço é  R$ {}.' .format (preço,  desconto,preço2))
