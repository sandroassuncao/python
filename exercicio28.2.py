from random import randint
from time import sleep
computador = randint(0,5) #Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar....')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei?'))# jogador tenta advinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABENS! Você conseguiu me vencer!')
else:
    print('GANHEI!Eu pensei no número {} e não no {}!'.format(computador,jogador))