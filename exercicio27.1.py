# Este código Python lê seu nome completo e mostra o primeiro e o último nome.

nome_completo = input("Digite seu nome completo: ")

# Divide o nome completo em uma lista de palavras.
palavras = nome_completo.split()

# O primeiro nome é a primeira palavra da lista.
primeiro_nome = palavras[0]

# O último nome é a última palavra da lista.
ultimo_nome = palavras[-1]

# Imprime o primeiro e o último nome.
print(f"Primeiro nome: {primeiro_nome}")
print(f"Último nome: {ultimo_nome}")

Use o código com cuidado. Saiba mais

Exemplo de execução:

Digite seu nome completo: José da Silva Oliveira
Primeiro nome: José
Último nome: Oliveira

Explicação do código:

    A linha nome_completo = input("Digite seu nome completo: ") lê o nome completo do usuário e o armazena na variável nome_completo.
    A linha palavras = nome_completo.split() divide o nome completo em uma lista de palavras, separadas por espaços.