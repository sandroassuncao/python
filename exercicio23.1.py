# Este código Python recebe um número inteiro e mostra a unidade, dezena, centena e milhar.

numero = int(input("Digite um número inteiro: "))

# Extraindo os dígitos
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

# Imprimindo os resultados
print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milhar}")
