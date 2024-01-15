
senha = ""

# O while tá sendo usado para o user entrar em looping se estiver errando a senha
while senha != "1234":
    # Solicita ao usuário para digitar a senha
    senha = input("Coloca sua senha de 4 digitos, mano da quebrada: ")
    # Verifica se a senha é correta
    if senha == "1234":
        print("Acertou, Mizeravi!")
    else:
        print("Burrão. Errou!")

print("Deu certo! Tu não tem alzeimer (sei lá como escreve!)")
