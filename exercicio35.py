salario = float(input('Qual é o seu salário?'))
if salario <= 1250:    
    novo = salario +(salario * 15/100)
else: 
    novo = salario +(salario * 10/100)
print('Quem ganha R${:.2f} passa a ganhar R${:.2f}'.format(salario,novo))