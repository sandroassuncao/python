# Programa para calcular o aumento de salário

salario = float(input("Digite o salário do funcionário: "))

if salario < 1250:
  aumento = salario * 0.15
else:
  aumento = salario * 0.1

novo_salario = salario + aumento

print(f"O funcionário que recebia R${salario:.2f}, receberá um aumento de R${aumento:.2f}.")
print(f"O novo salário será de R${novo_salario:.2f}.")
