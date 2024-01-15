
frutas = ["banana", "kiwi", "morango", "graviola", "uva"]


fruta_usuario = input("Mano, de novo você vai comprar frutas? O que você quer agora?").strip().lower()

# Se já estiver na lista..
if fruta_usuario in frutas:
    print("Mano, isso tá na lista já! Tá chapando?")
else:
    frutas.append(fruta_usuario)
    print("Essa não tá na lista. Coloquei pra você não me encher o saco!")

# Essa será a lista a pós o input do maluco
print("Tua lista tá assim, mano da quebrada:", frutas)
