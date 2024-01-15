# aprendi agora esse lance do def kkkk ele deve ser usado para definir uma função. Aqui, no caso, a função é substituir as vogais que aparecem na variável vogais
def substitui_vogais(frase):
    vogais = 'aeiouAEIOU'
    for vogal in vogais:
        frase = frase.replace(vogal, '*')
    return frase

# Exemplinho
frase_exemplo = "'Tony Balada' é um personagem de uma ficção onde o gato galático vira pistoleiro e mata seu amigo com uma batata frita."
frase_modificada = substitui_vogais(frase_exemplo)
print(frase_modificada)
