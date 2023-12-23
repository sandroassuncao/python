frase = str(input('Digite uma frase:')).upper().strip()
print('quantas vezes aparece a letra a:{}'.format(frase.count('A')))
print('a primeira letra a apareceu na posição: {}.'. format(frase.find('A')+1))
print('a ultima letra a apareceu na posição: {}'.format(frase.rfind('A')+1))