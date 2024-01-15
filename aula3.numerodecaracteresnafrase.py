
frase = input("Qual a frase, mano?: ")
palavras = frase.split()
for palavra in palavras:
    print(f"{palavra}: {len(palavra)} caracteres")
