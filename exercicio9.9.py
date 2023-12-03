real = float(input('quantos reais você tem? R$'))
dolar = real / 4.88
euro = real / 5.31 
print('com R${:.2f} você pode comprar US${:.2f} e EUR${:.2f}'.format (real,dolar,euro))