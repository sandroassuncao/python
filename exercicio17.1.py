import math

def main():
    # Leia o ângulo em graus
    angle = float(input("Digite o ângulo em graus: "))

    # Converta o ângulo para radianos
    radians = math.radians(angle)

    # Calcule o seno, cosseno e tangente
    sin = math.sin(radians)
    cos = math.cos(radians)
    tan = math.tan(radians)

    # Imprima os resultados
    print("O seno do ângulo é:", sin)
    print("O cosseno do ângulo é:", cos)
    print("A tangente do ângulo é:", tan)

if __name__ == "__main__":
    main()