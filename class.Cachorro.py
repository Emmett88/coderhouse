class Cachorro:
    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca

    def latir(self):
        print("Au!")

# Criando um objeto da classe Cachorro
meu_cachorro = Cachorro(nome='Rex', idade=5, raca='Labrador')
meu_cachorro.latir()  # Isso imprimirá "Au!" na saída
