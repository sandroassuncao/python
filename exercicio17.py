from math import radians,sin, cos , tan
angulo = float(input('Digite o angulo que você deseja:'))
seno = sin(radians(angulo))
print('O angulo de {} tem SENO de {}'.format(angulo,seno))
cosseno = cos(radians (angulo))
print('O angulo de {} tem o COSSENO de {}' .format(angulo, cosseno))
tangente = tan(radians (angulo))
print('o angulo  de {} tem a TANGENTE de {}'.format (angulo, tangente))