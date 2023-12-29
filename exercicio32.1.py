distancia = float(input('input(qual é a distancia da viagem?'))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço de sua passagem será de R${}'.format(preço))