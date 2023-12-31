# Programa para encontrar o maior e o menor entre 3 números

# Declarando as variáveis
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

# Inicializando as variáveis ​​de maior e menor com o primeiro número
maior = numero1
menor = numero1

# Verificando se o segundo número é maior ou menor que o maior
if numero2 > maior:
    maior = numero2
elif numero2 < menor:
    menor = numero2

# Verificando se o terceiro número é maior ou menor que o maior
if numero3 > maior:
    maior = numero3
elif numero3 < menor:
    menor = numero3

# Imprimindo o maior e o menor número
print("O maior número é:", maior)
print("O menor número é:", menor)

