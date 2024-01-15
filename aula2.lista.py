
lista = []


for i in range(5):
    while True:
        try:
            numero = int(input(f"Insira o {i+1}º número inteiro: "))
            lista.append(numero)
            break
        except ValueError:
            print("Por favor, insira um número inteiro válido.")


print("Lista de números inteiros:", lista)
