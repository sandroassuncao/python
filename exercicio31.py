numero = int(input('Digite um numero:')) 
resultado = numero % 2
if resultado == 0:
  print('o numero {} é par.'.format(numero))
else:
  print('O numero {} é impar'.format(numero))