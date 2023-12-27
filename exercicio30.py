v = float(input('Qual é a velocidade atual do carro?'))
if v > 80: 
 print('Você ultrapassou a velocidade permitida que é de 80km/h. Você foi MULTADO!')
 multa = (v-80)*7
 print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia e dirija com segurança!')