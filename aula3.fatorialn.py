def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

# Exemplo de uso da função
n = 10  # Você pode alterar este valor para testar com outros números
fatorial_de_n = calcular_fatorial(n)
print(fatorial_de_n)
