
# Q1

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a

def verifica_fibonacci(numero):
    if numero < 0:
        return f"O número {numero} não pertence à sequência de Fibonacci."
    elif numero == fibonacci(numero):
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

# Exemplo de uso:
numero = int(input("Informe um número: "))
resultado = verifica_fibonacci(numero)
print(resultado)


# Q2

def verificar_letra_a(string):
    # Converte a string para minúscula para facilitar a contagem
    string = string.lower()
    
    # Conta a ocorrência da letra 'a'
    contagem = string.count('a')
    
    if contagem > 0:
        print(f"A letra 'a' aparece {contagem} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

# Exemplo de uso:
string = input("Informe uma string: ")
verificar_letra_a(string)


